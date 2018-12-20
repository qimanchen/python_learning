#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_3
from ryu.controller import ofp_event
from ryu.controller.handler import set_ev_cls
from ryu.controller.handler import CONFIG_DISPATCHER
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.topology import event
from ryu.topology.api import get_switch
from ryu.topology.api import get_link

import networkx as nx


class ExampleShortestForwarding(app_manager.RyuApp):
    """"""

    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(ExampleShortestForwarding, self).__init__(*args, **kwargs)
        self.network = nx.DiGraph()
        self.topology_api_app = self
        self.paths = {}

    # handle switch features info
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        ofp_parser = datapath.ofproto_parser

        # install a table miss flow entry for each datapath
        match = ofp_parser.OFPMatch()
        actions = [ofp_parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                              ofproto.OFPCML_NO_BUFFER)]

        # install flow entry
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        ofp_parser = datapath.ofproto_parser

        # construct a flow_mod msg and send it to datapath
        inst = [ofp_parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                  actions)]
        mod = ofp_parser.OFPFlowMod(datapath=datapath, priority=priority,
                                    match=match, instructions=inst)
        datapath.send_msg(mod)

    # get topology and store it into network object
    @set_ev_cls(event.EventSwitchEnter, [CONFIG_DISPATCHER, MAIN_DISPATCHER])
    def get_topology(self, ev):
        # get nodes
        switch_list = get_switch(self.topology_api_app, None)
        switches = [switch.dp.id for switch in switch_list]
        self.network.add_nodes_from(switches)

        # get links
        links_list = get_link(self.topology_api_app, None)
        links = [(link.src.dpid, link.dst.dpid, {'port': link.src.port_no}) for link in links_list]
        self.network.add_edges_from(links)

        # reverse links
        links = [(link.dst.dpid, link.src.dpid, {'port': link.dst.port_no}) for link in links_list]
        self.network.add_edges_from(links)

    # get out_port by using networkx's Dijkstra algorithm
    def get_out_port(self, datapath, src, dst, in_port):
        dpid = datapath.id

        # add links between host and access switch
        if src not in self.network:
            self.network.add_node(src)
            self.network.add_edge(dpid, src)
            self.network[dpid][src].update({'port': in_port})
            # self.network.edges[dpid, src].update({'port': in_port})

            self.network.add_edge(src, dpid)
            self.paths.setdefault(src, {})

        # search dst's shortest path
        if dst in self.network:
            if dst not in self.paths[src]:
                path = nx.shortest_path(self.network, src, dst)
                self.paths[src][dst] = path
            path = self.paths[src][dst]
            next_hop = path[path.index(dpid) + 1]
            out_port = self.network[dpid][next_hop]['port']
            print "path:", path
        else:
            out_port = datapath.ofproto.OFPP_FLOOD

        return out_port

    # handler packet in msg
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        # get topology info.
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        ofp_parser = datapath.ofproto_parser

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocol(ethernet.ethernet)
        in_port = msg.match['in_port']

        # get out_port
        out_port = self.get_out_port(datapath, eth.src, eth.dst, in_port)
        actions = [ofp_parser.OFPActionOutput(out_port)]

        # install flow entry
        if out_port != ofproto.OFPP_FLOOD:
            match = ofp_parser.OFPMatch(in_port=in_port, eth_dst=eth.dst)
            self.add_flow(datapath, 1, match, actions)

        # send packet out msg to data path
        out = ofp_parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
                                      in_port=in_port, actions=actions)
        datapath.send_msg(out)

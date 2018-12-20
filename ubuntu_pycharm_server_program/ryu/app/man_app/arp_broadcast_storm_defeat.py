#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_3
from ryu.controller import ofp_event
from ryu.controller.handler import set_ev_cls
from ryu.controller.handler import CONFIG_DISPATCHER,MAIN_DISPATCHER
from ryu.lib.packet import packet,ethernet
from ryu.lib.packet import ether_types

class ArpBroadcastStorm(app_manager.RyuApp):
    """achieve simple switch for aviod broadcat storm"""
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self,*args,**kwargs):
        super(ArpBroadcastStorm,self).__init__(*args,**kwargs)
        # creat a dict for save host mac address
        self.mac_to_port = {}

    # handle switch connect controller( Hello )
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures,CONFIG_DISPATCHER)
    def switch_features_handler(self,ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # install a table miss flow entry to each switch
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath,0,match,actions)

    # add flow entry to switch
    def add_flow(self,datapath,priority,match,actions,buffer_id=None):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
        if buffer_id:
            mod = parser.OFPFlowMod(datapath=datapath,buffer_id=buffer_id,
                                    priority=priority,match=match,
                                    instructions=inst)
        else:
            mod = parser.OFPFlowMod(datapath=datapath,priority=priority,
                                    match=match,instructions=inst)

        datapath.send_msg(mod)

    # handle packet in event
    @set_ev_cls(ofp_event.EventOFPPacketIn,MAIN_DISPATCHER)
    def packet_in_handler(self,ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data)

        # parser eth adress
        eth = pkt.get_protocol(ethernet.ethernet)

        if eth.ethertype == ether_types.ETH_TYPE_LLDP:
            match = parser.OFPMatch(eth_type=eth.ethertype)
            actions = []
            self.add_flow(datapath,10,match,actions)
            return

        if eth.ethertype == ether_types.ETH_TYPE_IPV6:
            match = parser.OFPMatch(eth_type=eth.ethertype)
            actions = []
            self.add_flow(datapath,10,match,actions)
            return

        dst = eth.dst
        src = eth.src
        dpid = datapath.id

        self.logger.info("packet in %s %s %s %s",dpid,src,dst,in_port)
        self.mac_learning(datapath,src,in_port)

        # out_port determine
        if dst in self.mac_to_port[(datapath,datapath.id)]:
            out_port = self.mac_to_port[(datapath,datapath.id)][dst]
        else:
            if self.mac_learning(datapath,src,in_port) is False:
                out_port = ofproto.OFPPC_NO_RECV
            else:
                out_port = ofproto.OFPP_FLOOD

        actions = [parser.OFPActionOutput(out_port)]

        # determine the flow entry out_port
        if out_port != ofproto.OFPP_FLOOD:
            match = parser.OFPMatch(in_port=in_port,eth_dst=dst)
            if msg.buffer_id != ofproto.OFP_NO_BUFFER:
                self.add_flow(datapath,10,match,actions,msg.buffer_id)
                return
            else:
                self.add_flow(datapath,10,match,actions)

        data = None
        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data

        # handler this entry
        out = parser.OFPPacketOut(datapath=datapath,buffer_id=msg.buffer_id,
                                  in_port=in_port,actions=actions,data=data)
        datapath.send_msg(out)

    # mac learning
    def mac_learning(self,datapath,src,in_port):
        self.mac_to_port.setdefault((datapath,datapath.id),{})

        # learning a mac address to avoid FLOOD next time.
        if src in self.mac_to_port[(datapath,datapath.id)]:
            if in_port != self.mac_to_port[(datapath,datapath.id)][src]:
                return False
        else:
            self.mac_to_port[(datapath,datapath.id)][src] = in_port
            return True


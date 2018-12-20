#!/usr/bin/env python
#-*- coding: utf-8 -*-

from ryu.base import app_manager
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet


class L2Forwarding(app_manager.RyuApp):

    def __init__(self,*args,**kwargs):
        super(L2Forwarding,self).__init__(*args,**kwargs)

    #
    @set_ev_cls(ofp_event.EventOFPPacketIn,MAIN_DISPATCHER)
    def _packet_in_handler(self,ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocol(ethernet.ethernet)

        dst = eth.dst
        src = eth.srt

        out = ofp_parser.OFPPacketOut(datapath=dp,in_port=msg.in_port,actions=actions)
        dp.send_msg(out)

        msg = ev.msg
        in_port = msg.match['in_port']
        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocol(ethernet.ethernet)
        dst = eth.dst
        match = parser.OFPMatch(in_port=in_port,eth_dst=dst)

        actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)] # Build the required actions

        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,actions)]

        mod = parser.OFPFlowMod(datapath=datapath,priority=0,match,insturctions=inst)
        datapath.send_msg(mod)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example to create a Mininet topology and connect it to the internet via NAT
"""

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import lg, info
from mininet.node import OVSSwitch


class MyTopo(Topo):
    "Simple topology example."

    def __init__(self, k):
        "Create custom topo."

        # Initialize topology
        super(MyTopo, self).__init__()

        # add switch
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # add host and link for switch s1
        for i in range(k):
            host = self.addHost('a_s1_{}'.format(i+1))
            self.addLink(host, s1)

        # add host for switch s2
        for i in range(k):
            host = self.addHost('a_s2_{}'.format(i + 1))
            self.addLink(host, s2)

        self.addLink(s1, s2)


if __name__ == '__main__':
    lg.setLogLevel( 'info')
    man_topo = MyTopo(2)

    net = Mininet(man_topo)
    # Add NAT connectivity
    net.addNAT().configDefault()
    net.start()
    info( "*** Hosts are running and should have internet connectivity\n" )
    info( "*** Type 'exit' or control-D to shut down network\n" )
    CLI( net )
    # Shut down NAT
    net.stop()
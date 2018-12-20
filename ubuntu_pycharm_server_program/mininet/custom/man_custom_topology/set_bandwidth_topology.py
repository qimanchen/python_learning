#!/usr/bin/env python
# -*- coding: utf-8 -*-


from mininet.topo import Topo


class MyTopo(Topo):
    """Simple topology with bandwidth setting example"""

    def __init__(self, **opts):
        """Create custom topo"""

        # Initialize topology
        super(MyTopo, self).__init__(**opts)

        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s3 = self.addSwitch('s3')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add links
        self.addLink(h1,s1, bw=10)
        self.addLink(h2,s3, bw=20)
        self.addLink(s3,s2, bw=10)
        self.addLink(s1, s3, bw=10)


# for --topo mytopo instruction usage
topos = {'mytopo': (lambda: MyTopo())}

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info


def ToRealInet():
    """
        Test mininet link real internet.
        resource: https://www.cnblogs.com/cotyb/p/5161820.html
        Mininet 2.0 or the early version achieve way

    """
    net = Mininet(topo=None, build=False)

    info("*** Adding controller\n")
    net.addController(name='c0')

    info("*** Add switches\n")
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    info("*** Add hosts\n")
    h1 = net.addHost('h1', ip='0.0.0.0')
    h2 = net.addHost('h2', ip='0.0.0.0')
    h3 = net.addHost('h3', ip="10.0.2.1")

    info("*** Add links\n")
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(s1, s2)

    info("*** Starting network\n")
    net.start()
    os.popen("ovs-vsctl add-port s1 eth1")  #
    h1.cmdPrint("dhclient " + h1.defaultIntf().name)  # h1 interface for auto diverse DHCP -> ip
    h2.cmdPrint("dhclient " + h2.defaultIntf().name)
    # h3.cmdPrint("dhclient " + h3.defaultIntf().name)
    CLI(net)
    net.stop()


if __name__ == "__main__":
    setLogLevel('info')
    ToRealInet()

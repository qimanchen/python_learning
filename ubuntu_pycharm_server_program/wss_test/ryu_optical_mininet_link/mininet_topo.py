#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
设置mininet虚拟拓扑网络与实际物理网络拓扑相连
__start_time = 2018/12/17
__author = Qiman Chen
"""
import re

from mininet.log import setLogLevel, info, error
from mininet.util import quietRun
from mininet.topo import Topo


class MyTopo(Topo):

    def __init__(self):
        """Create custom topo"""

        super(MyTopo, self).__init__()

        # add switch
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # add host and link for switch s1
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # add link
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(s1, s2)

    @staticmethod
    def check_intf(intf):
        """Make sure intf exists and is not configured."""
        config = quietRun('ifconfig %s 2>/dev/null'% intf, shell=True)

        if not config:
            error('Error', intf, 'does not exist!\n')
            exit(1)
        ips = re.findall(r'\d+\.\d+\.\d+\d+', config)
        if ips:
            error('Error:', intf, 'has an IP address, and is probably in use!\n')
            exit(1)


def my_test(net):
    pass


# 设置自定义topo的输入参数
topos = {'mytopo': MyTopo}
tests = {'mytest': my_test}
"""
命令行调试 --> 设置自定义topo调用
sudo mn --custom mytopo.py --topo mytopo, para1, para2,... --test mytest
"""


if __name__ == '__main__':
    setLogLevel('info')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from lxml import etree


if __name__ == '__main__':
    # with open("netconf_wss_msg/get_config_all_disabled_ports", "r") as f:
    #     result = f.read()
    #
    # print(result)
    tree = etree.parse(r"netconf_wss_msg/get_config_all_disabled_ports")
    rpc_reply = etree.tostring(tree, encoding="unicode", pretty_print=True)
    print(rpc_reply)



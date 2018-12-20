#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""通过 netconf 数据包连接上了光开光
__time: 2018_11_13
"""

from netconf.client import NetconfSSHSession
from netconf.client import NetconfClientSession
from lxml import etree
import re
from netconf import util

PORTS_NAMESPACE = "{http://www.polatis.com/yang/optical-switch}"
# port-id,port-state
# http://www.polatis.com/yang/optical-switch
# ingress, egress


class GetInfo(object):
    """ Get optical switch configure info by netconf's get function"""
    def __init__(self, host="192.169.3.200", port=830, username="admin", password="root"):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.__session = None

    def open_ssh_link(self):
        self.__session = NetconfSSHSession(self.host, self.port, self.username, self.password)

    def close_ssh_link(self):
        self.__session.close()

    def get_config_info(self):
        root_info = self.__session.get_config()
        ingress_list = [i.text for i in root_info.iter('{http://www.polatis.com/yang/optical-switch}ingress')]
        egress_list = [i.text for i in root_info.iter('{http://www.polatis.com/yang/optical-switch}egress')]
        port_id = []
        count = 0
        ports_status = {}
        # ports_status = [{i.text: j.text}
        #                 for i in root_info.iter('{http://www.polatis.com/yang/optical-switch}port-id')
        #                 for j in root_info.iter('{http://www.polatis.com/yang/optical-switch}port-state')
        #                 if j.text != "PC_ENABLED"]
        # for i in root_info.iter('{http://www.polatis.com/yang/optical-switch}port-id'):
        #     port_id.append(int(i.text))

        for j in root_info.iter('{http://www.polatis.com/yang/optical-switch}port-state'):
            count += 1
            if j.text != "PC_ENABLED":
                ports_status[str(count)] = j.text
        return ingress_list, egress_list, ports_status

    def edit_config_delete(self):
        """ delete a connect
        <data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        """
        # # ******** delete connect ********
        # query = """<edit-config>
        # <target>
        # <running/>
        # </target>
        # <default-operation>none</default-operation>
        # <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
        # <cross-connects xmlns="http://www.polatis.com/yang/optical-switch">
        # <pairs xc:operation="delete">
        # <ingress>3</ingress>
        # <egress>27</egress>
        # </pairs>
        # </cross-connects>
        # </config>
        # </edit-config>"""

        # modify the port state to disabled
        # query = """<edit-config>
        # <target>
        # <running/>
        # </target>
        # <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
        # <ports xmlns="http://www.polatis.com/yang/optical-switch">
        # <port>
        # <port-id>1</port-id>
        # <port-label/>
        # <port-state>PC_DISABLED</port-state>
        # <peer-port/>
        # </port>
        # </ports>
        # </config>
        # </edit-config>
        # """

        # ******** create a connect ********
        # query = """<edit-config>
        # <target>
        # <running/>
        # </target>
        # <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
        # <cross-connects xmlns="http://www.polatis.com/yang/optical-switch">
        # <pairs>
        # <ingress>3</ingress>
        # <egress>27</egress>
        # </pairs>
        # </cross-connects>
        # </config>
        # </edit-config>"""

        # get-config the all connected
        # query = """<get-config>
        # <source>
        # <running/>
        # </source>
        # <filter type="subtree">
        # <cross-connects xmlns="http://www.polatis.com/yang/optical-switch">
        # <pairs />
        # </cross-connects>
        # </filter>
        # </get-config>
        #         """

        # get-config the all disabled ports
        query = """<get-config>
        <source>
        <running/>
        </source>
        <filter type="subtree">
        <ports xmlns="http://www.polatis.com/yang/optical-switch">
        <port>
        <port-state>PC_DISABLED</port-state>
        </port>
        </ports>
        </filter>
        </get-config>
        """

        # interface enable -> disable

        # reply = self.__session.edit_config(method="none", newconf=conf)
        _, reply, _ = self.__session.send_rpc(query)

        rpc_reply = etree.tostring(reply, encoding="unicode", pretty_print=True)
        print(rpc_reply)

    def get_ingress_list(self):
        pass

    def get_egress_list(self):
        pass

    def get_connect(self):
        pass


class SetWss(object):
    pass


def wss_get():
    session = NetconfSSHSession(host='192.169.3.200', port=830, username='admin', password='root')

    # config = session.get(select="/ports/port/peer-port")
    result = session.get_config()
    result = etree.tostring(result, encoding="unicode")
    # <cross-connects xmlns="http://www.polatis.com/yang/optical-switch">
    #     <pairs>
    #       <ingress>1</ingress>
    #       <egress>25</egress>
    #     </pairs>
    #   </cross-connects>
    print(result)
    result2 = re.match(r"^.*(<cross-connects.*</cross-connects>).*$", result)
    print(result2.group(1))
    result3 = re.search(r"<cross-connects.*</cross-connects>", result, re.M | re.I)
    print(result3.group())
    session.close()


def test_xpath_filter_result():
    session = NetconfSSHSession(host='192.169.3.200', port=830, username='admin', password='root')

    result = session.get_config()

    # data = etree.tostring(result, encoding="unicode")
    # print(data)
    # for child in result:
    #     print(child.tag, child.attrib)
    # 得到的结果：
    # {http: // www.polatis.com / yang / optical - switch}ports
    # {}
    # {http: // www.polatis.com / yang / optical - switch}cross - connects
    # {}
    # {http: // www.polatis.com / yang / optical - switch}system - config
    # {}
    # {http: // www.polatis.com / yang / polatis - switch}enable - notifications
    # {}
    # {urn: ietf: params:xml: ns:yang: ietf - netconf - acm}nacm
    # {}

    for neighbor in result.iter('{http://www.polatis.com/yang/optical-switch}ingress'):
        print(neighbor.text)

    for neighbor in result.iter('{http://www.polatis.com/yang/optical-switch}egress'):
        print(neighbor.text)

    # for pairs in result.findall(r'pairs'):
    #     print(pairs.find('ingress').text)

    # print(result.xpath("string()"))

    # 通过索引的方式是可行的
    # print(result[1][0][0].text)
    # print(result[1][0][1].text)

    session.close()


def test_NetconfClientSession():
    session = NetconfClientSession()


if __name__ == '__main__':
    test_conn = GetInfo()
    test_conn.open_ssh_link()
    test_conn.edit_config_delete()
    test_conn.close_ssh_link()

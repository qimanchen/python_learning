#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
optical switch communication with controller(ryu) by netconf package
reference protocol: rfc4741
__start_time = 2018/12/14
__author = Chen Qiman
__version_1_time = 2018/12/17
"""

from netconf.client import NetconfSSHSession
from lxml import etree
import re
import logging
import time


PORT_STATE = ["PC_ENABLED", "PC_DISABLED"]
logger = logging.getLogger("NetconfAgent")


def set_test_loggin():
    logger = logging.getLogger("NetconfAgent")
    logger.setLevel(logging.DEBUG)
    # 设置一个filehandler来记录日志
    # log_file = logging.FileHandler("debug.log")
    # log_file.setLevel(logging.DEBUG)

    # 控制台输出logging信息
    cmd_info = logging.StreamHandler()
    cmd_info.setLevel(logging.DEBUG)
    # 设置输出信息格式
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s:%(name)s:%(message)s")
    cmd_info.setFormatter(formatter)
    # 将相应的handler添加到logger对象中
    logger.addHandler(cmd_info)
    # logger = logging.getLogger('paramiko.transport')


class NetconfAgent(object):
    """ netconf agent for communication with ryu"""

    def __init__(self, host="192.169.3.200", port=830, username="admin", password="root"):
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__session = None
        self.exist_connect = {}
        self.ports_state = {}

    def open_ssh_link(self):
        """create a tcp communication link with OptcialSwitch by netconf protocol"""
        self.__session = NetconfSSHSession(self.__host, self.__port,
                                           self.__username, self.__password)
        logger.info("Optical Switch connect is created！")

    def close_ssh_link(self):
        """close the netconf link with OpticalSwitch"""
        self.__session.close()
        logger.info("Optical Switch connect is closed!")

    def send_rpc_info(self, query):
        """send rpc request for get info from OpticalSwitch"""
        _, reply, _ = self.__session.send_rpc(query)
        # rpc_reply = etree.tostring(reply, encoding="unicode", pretty_print=True)
        rpc_reply = etree.tostring(reply)
        return reply, rpc_reply

    def get_config_info(self):
        """Get all config information from OpticalSwitch"""
        query = """<get-config>
        <source>
        <running/>
        </source>
        </get-config>
        """
        logger.info("Start deal get_config")
        reply, reply_get_config_info = self.send_rpc_info(query)
        # ingress_nodes = [ingress_node.text
        #                  for ingress_node
        #                  in reply.iter("{http://www.polatis.com/yang/optical-switch}ingress")]
        # egress_nodes = [egress_node.text
        #                 for egress_node
        #                 in reply.iter("{http://www.polatis.com/yang/optical-switch}ingress")]
        # port_states = [port_state.text
        #                for port_state in reply.iter("{http://www.polatis.com/yang/optical-switch}port-state")]
        # print port_states
        # print ingress_nodes
        # print egress_nodes

        logger.info("Start parse get_config info")
        # get all connects in OpticalSwitch
        all_connects = [etree.tostring(test)
                        for test in reply.iter("{http://www.polatis.com/yang/optical-switch}pairs")]
        # self.exist_connect = {}
        for port_state in all_connects:
            re_match = re.match(r'.*?<ingress>(\d+?)</ingress><egress>(\d+?)</egress>.*', str(port_state))
            self.exist_connect[re_match.group(1)] = re_match.group(2)
        logger.info("This exist link include: {0}".format(self.exist_connect))

        # get all disabled ports
        all_port_state = [etree.tostring(test)
                          for test in reply.iter("{http://www.polatis.com/yang/optical-switch}port")]
        # ports_state = {}
        for port_state in all_port_state:
            re_match = re.match(r'.*?<port-id>(\d+?)</port-id>.*?<port-state>(.*?)</port-state>.*', str(port_state))
            if re_match.group(2) == "PC_DISABLED":
                self.ports_state[re_match.group(1)] = re_match.group(2)
        logger.info("These are all disabled ports: {0}".format(self.ports_state))

    def get_info(self):
        """Get all info from OpticalSwitch"""
        query = """<get/>"""
        reply, reply_get_info = self.send_rpc_info(query)
        logger.info(reply_get_info)

    def get_all_disabled_ports(self):
        """Get all disabled ports in OpticalSwitch"""
        query = """<get-config>
        <source>
        <running/>
        </source>
        <filter type="subtree">
        <ports xmlns="http://www.polatis.com/yang/optical-switch">
        <port/> 
        </ports>
        </filter>
        </get-config>
        """
        reply, reply_info = self.send_rpc_info(query)
        # get all disabled ports
        all_port_state = [etree.tostring(test)
                          for test in reply.iter("{http://www.polatis.com/yang/optical-switch}port")]
        # ports_state = {}
        for port_state in all_port_state:
            re_match = re.match(r'.*?<port-id>(\d+?)</port-id>.*?<port-state>(.*?)</port-state>.*', str(port_state))
            if re_match.group(2) == "PC_DISABLED":
                self.ports_state[re_match.group(1)] = re_match.group(2)
        logger.info("These all disabled port is:\n{0}!".format(self.ports_state))

    def get_all_connect(self):
        """Get all optical link in OpticalSwitch"""
        query = """<get-config>
                <source>
                <running/>
                </source>
                <filter type="subtree">
                <cross-connects xmlns="http://www.polatis.com/yang/optical-switch">
                <pairs/>
                </cross-connects> 
                </filter>
                </get-config>
                """
        reply, reply_info = self.send_rpc_info(query)
        # get all connects in OpticalSwitch
        all_connects = [etree.tostring(test)
                        for test in reply.iter("{http://www.polatis.com/yang/optical-switch}pairs")]
        # self.exist_connect = {}
        for port_state in all_connects:
            re_match = re.match(r'.*?<ingress>(\d+?)</ingress><egress>(\d+?)</egress>.*', str(port_state))
            self.exist_connect[re_match.group(1)] = re_match.group(2)
        logger.info("All exist link is:\n{0}!".format(self.exist_connect))

    def delete_one_connect(self, ingress_port, egress_port):
        """delete one exist connect in OpticalSwitch"""
        if egress_port < ingress_port:
            ingress_port, egress_port = egress_port, ingress_port
        if str(ingress_port) not in self.exist_connect:
            logger.info("{0} with {1} connect isn't exist!".format(ingress_port, egress_port))
            return
        query = """<edit-config>
        <target>
        <running/>
        </target>
        <default-operation>none</default-operation>
        <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <cross-connects xmlns="http://www.polatis.com/yang/optical-switch">
        <pairs xc:operation="delete">
        <ingress>{0}</ingress>
        <egress>{1}</egress>
        </pairs>
        </cross-connects>
        </config>
        </edit-config>""".format(ingress_port, egress_port)
        reply, reply_info = self.send_rpc_info(query)
        # if delete connect is success it will be return one OK info!
        re_reply_info = re.match(r'.*?(ok).*', str(reply_info))
        if re_reply_info and re_reply_info.group(1) == 'ok':
            self.exist_connect.pop(str(ingress_port))
            logger.info("{0} with {1} connect is deleting successful".format(ingress_port, egress_port))

    def add_one_connect(self, ingress_port, egress_port):
        """ add a new connect
        ingress_port --> egress_port or
        egress_port --> ingress_port
        """
        if egress_port < ingress_port:
            ingress_port, egress_port = egress_port, ingress_port
        if str(ingress_port) in self.exist_connect:
            logger.info("{0} with {1} connect is exist!".format(ingress_port, egress_port))
            return
        query = """<edit-config>
        <target>
        <running/>
        </target>
        <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <cross-connects xmlns="http://www.polatis.com/yang/optical-switch">
        <pairs>
        <ingress>{0}</ingress>
        <egress>{1}</egress>
        </pairs>
        </cross-connects>
        </config>
        </edit-config>""".format(ingress_port, egress_port)
        reply, reply_info = self.send_rpc_info(query)
        # print reply_info
        # parse if the connect is successful
        # print "Test reply"

        # Note: the reply_info isn't the encode string
        re_reply_info = re.match(r'.*?(ok).*', str(reply_info))
        if re_reply_info and re_reply_info.group(1) == 'ok':
            logger.info("{0} with {1} connect is creating successful".format(ingress_port, egress_port))

    def modify_port_state(self, port_id, port_state):
        # TODO 这里有个问题 -- port 的状态不能立马更新
        if ((str(port_id) in self.ports_state) and port_state == PORT_STATE[1]) or\
                ((str(port_id) not in self.ports_state) and port_state == PORT_STATE[0]):
            logger.info("port{0} state is already setted {1}".format(port_id, port_state))
            return
        query = """<edit-config>
        <target>
        <running/>
        </target>
        <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <ports xmlns="http://www.polatis.com/yang/optical-switch">
        <port>
        <port-id>{0}</port-id>
        <port-label/>
        <port-state>{1}</port-state>
        <peer-port/>
        </port>
        </ports>
        </config>
        </edit-config>""".format(port_id, port_state)
        reply, reply_info = self.send_rpc_info(query)

        # Note: the reply_info isn't the encode string
        re_reply_info = re.match(r'.*?(ok).*', str(reply_info))
        if re_reply_info and re_reply_info.group(1) == 'ok':
            logger.info("port-{0} state is changed to {1}".format(port_id, port_state))
        if port_state == PORT_STATE[0]:
            self.ports_state.pop(str(port_id))

    def get_hello_info(self):
        pass

    def system_restart(self):
        """ disconnect all connect and set all port with enabled"""
        pass


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s")
    # 设置测试logging
    # logger = logging.getLogger("NetconfAgent")
    logger.setLevel(logging.DEBUG)
    cmd_info = logging.StreamHandler()
    cmd_info.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s]  %(levelname)s: %(name)s: %(message)s")
    cmd_info.setFormatter(formatter)
    logger.addHandler(cmd_info)

    new_session = NetconfAgent()
    new_session.open_ssh_link()

    # new_session.get_config_info()
    new_session.get_all_connect()
    new_session.get_all_disabled_ports()

    new_session.delete_one_connect(2, 26)
    new_session.add_one_connect(3, 27)
    new_session.modify_port_state(2, PORT_STATE[0])
    # time.sleep(5)
    # new_session.get_config_info()
    new_session.get_all_connect()

    new_session.close_ssh_link()
    # 设置8秒使得其状态更新
    new_session.open_ssh_link()
    # time.sleep(5)
    new_session.get_all_disabled_ports()

    new_session.close_ssh_link()

#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ryu.lib.of_config.capable_switch import OFCapableSwitch
import ryu.lib.of_config.classes as ofc


if __name__ == '__main__':
    sess = OFCapableSwitch(host='192.169.3.200', port=830, username='admin', password='root')

    csw = sess.get()
    for p in csw.resources.port:
        print p.resource_id, p.current_rate

    csw = sess.get_config('running')
    for p in csw.resources.port:
        print p.resource_id, p.configuration.admin_state

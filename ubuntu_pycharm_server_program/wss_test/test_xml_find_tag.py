#!/usr/bin/env python
# -*- coding: utf-8 -*-


from lxml import etree
import re

query1 = '<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="0"><ok/></rpc-reply>'
query2 = """
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="0"><rpc-error>
<error-type>protocol</error-type>
<error-tag>unknown-element</error-tag>
<error-severity>error</error-severity>
<error-path>
/rpc/edit-config/target
</error-path><error-info><bad-element>target</bad-element>
</error-info>
</rpc-error>
</rpc-reply>
"""
root = etree.XML(query1)

root = etree.tostring(root)
re_root = re.match(r'.*?(ok).*',root)
if re_root:
    print re_root.groups()
    print re_root.group(1)

#!/usr/bin/env python
from __future__ import print_function

from jnpr.junos import Device
from getpass import getpass
from lxml import etree


pwd = getpass()

juniper_srx = {
    "host": "srx1.twb-tech.com",
    "user": "pyclass",
    "password": pwd,
}


def main():
    for device in [juniper_srx]:
        dev_connect = Device(**device)
        dev_connect.open()

        # output = dev_connect.cli('show lldp neighbors | display xml rpc',format='text', warning=True)
        # result to running the command was an element called: get-lldp-neighbors-information
        # Convert this tag to a rpc method call with underscores.  
        show_neighbors = dev_connect.rpc.get_lldp_neighbors_information()
        xml_output = etree.tostring(show_neighbors, encoding='unicode')
        print(xml_output)


if __name__ == '__main__':
    main()

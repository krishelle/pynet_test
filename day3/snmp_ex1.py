#!/usr/bin/env python

from __future__ import print_function
from snmp_helper import (snmp_get_oid, snmp_extract)
import getpass

SYS_DESCR = '1.3.6.1.2.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'

def main():
    """
    Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and
    prints out both the MIB2 sysName and sysDescr
    """
    try:
        ip_addr1 = raw_input("pynet-rtr1 IP address: ")
        ip_addr2 = raw_input("pynet-rtr2 IP address: ")
    except NameError:
        ip_addr1 = input("pynet-rtr1 IP address: ")
        ip_addr2 = input("pynet-rtr2 IP address: ")
    community_string = getpass.getpass(prompt="Community string: ")

    # The library requires this type of tuple.
    # SYNTAX: (ip_addr, comm_string, SNMP default port)
    pynet_rtr1 = (ip_addr1, community_string, 161)
    pynet_rtr2 = (ip_addr2, community_string, 161)

    for device in [pynet_rtr1, pynet_rtr1]:
        print("\n************************")
        for oid in [SYS_NAME, SYS_DESCR]:
            snmp_data = snmp_get_oid(device, oid=oid)
            output = snmp_extract(snmp_data)
            print(output)
        print("\n************************")
    print()

if __name__ == "__main__":
    main()


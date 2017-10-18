#!/usr/bin/env python
"""
SNMP query all of the interfaces on the pynet-rtr1 using SNMPv3.
Get the interface description and the in_octets/out_octets

Relevant Base OIDs are:

IFDESCR = '1.3.6.1.2.1.2.2.1.2.'
IFINOCTETS = '1.3.6.1.2.1.2.2.1.10.'
IFOUTOCTETS = '1.3.6.1.2.1.2.2.1.16.'

The last digit of the OID will range from 1 to 7 (for the different interfaces on this
device).
"""

from __future__ import print_function
from getpass import getpass
from snmp_helper import snmp_extract, snmp_get_oid_v3

IFDESCR = '1.3.6.1.2.1.2.2.1.2.'
IFINOCTETS = '1.3.6.1.2.1.2.2.1.10.'
IFOUTOCTETS = '1.3.6.1.2.1.2.2.1.16.'

def main():
    my_key = getpass(prompt="Auth + Encryption: ")

    ip_addr = '184.105.247.70'
    user = 'pysnmp'
    auth_key = my_key
    encrypt_key = my_key
    snmp_user = (user, auth_key, encrypt_key)
    pynet_rtr1 = (ip_addr, 161)

    print("{:>15} {:>15} {:>15}".format("IfDescr", "IfInOctets", "IfOutOctets"))

    for index in range(1,8):
        results = []
        for oid in [IFDESCR, IFINOCTETS, IFOUTOCTETS]:
            new_oid = oid + str(index)
            snmp_data = snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=new_oid)
            results.append(snmp_extract(snmp_data))
        print("{:>15} {:>15} {:>15}".format(*results))

if __name__ == '__main__':
    main()

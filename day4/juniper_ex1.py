#!/usr/bin/env python
from __future__ import print_function
from getpass import getpass
from jnpr.junos import Device

pwd = getpass("Enter password: ")

juniper_srx = {
    'host': 'srx1.twb-tech.com',
    'user': 'pyclass',
    'password': pwd

}

def main():
    """
    Use Juniper's PyEZ library to retrieve facts from the Juniper SRX
    """
    for device in [juniper_srx]:
        jun_dev = Device(**device)
        jun_dev.open()
        print(jun_dev.facts)

if __name__ == '__main__':
    main()

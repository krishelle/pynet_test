#!/usr/bin/env python

"""
a. Connect to the Juniper SRX
b. Configure + commit the following change to the SRX.

    set system syslog file messages any error
"""

from __future__ import print_function
from netmiko import ConnectHandler
from getpass import getpass

def main():
    password = getpass("Password: ")

    juniper1 = {
        'device_type': 'juniper_junos',
        'host': 'srx1.twb-tech.com',
        'username': 'pyclass',
        'password': password,
    }

    cmd = [
        'set system syslog file messages any error',
    ]

    net_connect = ConnectHandler(**juniper1)
    print('Connected to {} device, host {}'.format(juniper1['device_type'], juniper1['host']))
    cmd_result = net_connect.send_config_set(cmd)
    cmd_result += net_connect.commit()
    print()
    print(cmd_result)

if __name__ == '__main__':
    main()

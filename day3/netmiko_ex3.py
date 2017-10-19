#!/usr/bin/env python
from __future__ import print_function

import yaml
from netmiko import ConnectHandler
from getpass import getpass

def main():
    with open('netmiko.yml') as f:
        yaml_data = yaml.load(f)

    password = getpass()
    for device in yaml_data:
        print(device)
        device_name = device.pop('device_name')
        device['password'] = password
        net_connect = ConnectHandler(**device)
        print (net_connect.send_command('show arp'))
        net_connect.disconnect()
    print()

if __name__ == '__main__':
    main()

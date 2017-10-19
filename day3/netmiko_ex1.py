#!/usr/bin/env python

from __future__ import print_function
from getpass import getpass
from netmiko import ConnectHandler

def main():
    password = getpass()
    
    pynet_rtr1 = {
        'device_type': 'cisco_ios',
        'ip':   '184.105.247.70',
        'username': 'pyclass',
        'password': password,
    }

    srx = {
        'device_type': 'juniper_junos',
        'ip':   '184.105.247.76',
        'username': 'pyclass',
        'password': password,
    }
    devices = (pynet_rtr1, srx)

    for device in devices:
    	net_connect = ConnectHandler(**device)
	print("Current Prompt: ", net_connect.find_prompt())
        # user send_command to retrieve show version from two devices.
        version = net_connect.send_command('show version')
        print()
        print(version)
        print()
        
        show = None
        # use send_command to retrieve running config from devices
        if 'cisco' in device['device_type']:
            show = net_connect.send_command('show run')
        elif 'juniper' in device['device_type']:
            show = net_connect.send_command('show configuration')
        filename = net_connect.base_prompt + ".txt"
        print("Saving run output to: {}\n".format(filename))

        with open(filename, 'w') as f:
            f.write(show)

if __name__ == '__main__':
    main()

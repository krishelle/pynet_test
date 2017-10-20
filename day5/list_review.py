#!/usr/bin/env python
from __future__ import print_function

IP_ADDRESSES = [
    '52.53.239.109',
    '52.53.239.110',
    '52.53.239.111',
    '52.53.239.112',
    '52.53.239.113',
]

ROUTERS = {
    'rtr1' : {'ip_addr': '52.53.239.109', 'device_type': 'juniper_srx'},
    'rtr2' : {'ip_addr': '52.53.239.110', 'device_type': 'cisco_ios'},
    'rtr3' : {'ip_addr': '52.53.239.111', 'device_type': 'arista_eos'},
}

def print_ips():
    for ip in IP_ADDRESSES:
        print('This is my IP: {}'.format(ip))

def print_routers():
    for router, attrs in ROUTERS.items():
        print('Router: {}'.format(router))
        print('{:>20} {:>20}'.format("IP address:", attrs['ip_addr']))
#        print('\tIP address: {}'.format(attrs['ip_addr']))
        print('\tDevice type: {}'.format(attrs['device_type']))

def main():
    print_routers()


if __name__ == '__main__':
    main()

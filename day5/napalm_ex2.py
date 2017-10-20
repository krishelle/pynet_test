#!/usr/bin/env python
from __future__ import print_function
from pprint import pprint

from napalm_base import get_network_driver
from my_devices_na import juniper1, juniper2, cisco_rtr1

def main():
    for device in (juniper1, juniper2, cisco_rtr1):
        device_type = device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**device)

        print()
        print(">>>Device open")
        device.open()

        print("-" * 50)
        neighbors = device.get_lldp_neighbors()
        pprint(neighbors)

if __name__ == '__main__':
    main()


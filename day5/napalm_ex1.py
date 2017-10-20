#!/usr/bin/env python
from __future__ import print_function

from napalm_base import get_network_driver
from my_devices_na import device_list

def main():
    for device in device_list:
        device_type = device.pop('device_type')
        driver = get_network_driver(device_type) # returns a driver class specific to type.
        device = driver(**device)

        print()
        print(">>>Device Open")
        device.open()

        print("-" * 50)
        device_facts = device.get_facts() # this is using a napalm getter.
        print("{hostname}: Model={model}".format(**device_facts)) # can do this with kwargs

if __name__ == '__main__':
    main()

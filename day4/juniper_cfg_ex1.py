#!/usr/bin/env python
from __future__ import print_function
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass


pwd = getpass("Enter password: ")

juniper_dev = {
    "host": "juniper1.twb-tech.com",
    "user": "pyclass",
    "password": pwd,
}

def main():
    for device in [juniper_dev]:
        dev_connect = Device(**device)
        dev_connect.open()
        dev_connect.timeout = 90
        cfg = Config(dev_connect) # have to feed in the Juniper device object not dict. 

        # configure_ip.conf is a file in this directory that has the change in it.
        cfg.load(path="configure_ip.conf", format="text", merge=False)
        print(cfg.diff())

        cfg.commit()

if __name__ == '__main__':
    main()

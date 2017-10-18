#!/usr/bin/env python
"""
Write a Python program using ciscoconfparse that parses the 'cisco_ipsec.txt'
config file. Note, this config file is not fully valid (i.e. parts of the
configuration are missing).

The script should find all of the crypto map entries in the file (lines that
begin with 'crypto map CRYPTO') and print out the children of each crypto map.
"""
from __future__ import print_function, unicode_literals
from ciscoconfparse import CiscoConfParse

def main():
    cisco_file = '/home/student13/pynet-ons-oct17/day3/cisco_ipsec.txt'

    # Use this library to parse the file, since it has a space based hierarchy.
    cisco_cfg = CiscoConfParse(cisco_file)
    maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")
    
    for c_map in maps:
        print()
        print(c_map.text)
        for child in c_map.children:
            print(child.text)
        print()
if __name__ == '__main__':
    main()

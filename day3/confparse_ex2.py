#!/usr/bin/env python
"""
Use the ciscoconfparse library to find the crypto maps that are using pfs group2
"""

from __future__ import print_function
from ciscoconfparse import CiscoConfParse

def main():
    cisco_file = '/home/student13/pynet-ons-oct17/day3/cisco_ipsec.txt'
    cisco_cfg = CiscoConfParse(cisco_file)

    # Returns a list of child objects
    children = cisco_cfg.find_objects_w_child(childspec=r'pfs group2', parentspec=r'crypto map CRYPTO')
    print('\nCrypto Maps using PFS group 2:')
    for child in children:
        print('  {}'.format(child.text))
    print()

if __name__ == '__main__':
    main()

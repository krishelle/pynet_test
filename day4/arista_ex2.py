#!/usr/bin/env python
from __future__ import print_function
import pyeapi

"""
Execute 'show interfaces' on the Arista switch using eapi.

Extract the interfaceCounters inOctets/outOctets for all the interfaces
that have this information.
"""

def main():
    arista_sw = pyeapi.connect_to('pynet-sw4')
    output = arista_sw.enable('show interfaces')[0]
    output = output['result']['interfaces']


    print("\n{:>15} {:>15} {:>15}".format("Interface", "inOctets", "outOctets"))
    sep = '-' * 15
    print("{:>15} {:>15} {:>15}".format(sep, sep, sep))
    for interface, attrs in output.items():
        inter_cntr = attrs.get('interfaceCounters', 'None!')
        if inter_cntr == 'None!':
            in_octets = 0
            out_octets = 0
        else:
            in_octets = attrs['interfaceCounters']['inOctets']
            out_octets = attrs['interfaceCounters']['outOctets']
        print("{:>15} {:>15} {:>15}".format(interface, in_octets, out_octets))
if __name__ == '__main__':
    main()



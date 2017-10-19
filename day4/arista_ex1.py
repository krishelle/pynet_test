#!/usr/bin/env python

from __future__ import print_function
import pyeapi

def main():
    host_name = 'arista1.twb-tech.com'
    username = 'pyclass'
    ip = '184.105.247.72'

    arista_sw = pyeapi.connect_to("pynet-sw4")
    output = arista_sw.enable("show ip route")[0] # this returns a list containing a dictionary.
    
    output = output['result']['vrfs']['default']
    routes = output['routes']

    print("\n{:>15} {:>15} {:>15}".format("Prefix", "Next Hop", "Interface"))
    filler = "-" * 15
    print("{:>15} {:>15} {:>15}".format(filler, filler, filler))
    for prefix, attr in routes.items():
        next_hop = attr['vias'][0].get('nexthopAddr')
        interface = attr['vias'][0].get('interface')
        print("{:>15} {:>15} {:>15}".format(prefix, next_hop, interface))
    print()

if __name__ == '__main__':
    main()

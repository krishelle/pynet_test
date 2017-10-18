from __future__ import print_function
import re
from pprint import pprint


with open('show_mac_multicast.txt') as f:
    output = f.read()
output.strip()
mac = output.splitlines()[3].strip()

pattern = '(?P<vlan>\d+)\s+(?P<mac_addr>.*)\s+(?P<type>\w+)\s+(?P<ports>.*)'
regex = re.search(pattern, mac)
mac_dict = regex.groupdict()

formatted = { 
            mac_dict['mac_addr'].strip(): {
                'vlan': int(mac_dict['vlan']),
                'type': mac_dict['type'],
                'ports': mac_dict['ports'],
                }
            }

pprint(formatted)

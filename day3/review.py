#!/usr/bin/env python

from __future__ import print_function
from pprint import pprint
import os

with open('/home/student13/pynet-ons-oct17/day2/show_arp.txt') as f:
    output = f.read()

output = output.split('Interface')[1].strip()

my_dict = {}
for line in output.splitlines():
    components = line.strip().split()
    my_dict[components[1]] = components[3]

pprint(my_dict)

my_dict2 = {}
for line in output.splitlines():
    components = line.strip().split()
    my_dict2[components[3]] = components[1]
pprint(my_dict2)


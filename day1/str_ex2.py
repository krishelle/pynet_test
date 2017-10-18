#!/usr/bin/env python
from __future__ import print_function

try:
    ip = raw_input("Please enter an IP address: ")
except SyntaxError:
    print("Syntax error, please try again")
    ip = input("Please enter an IP address: ")
octets = ip.split('.')
octets[-1] = 0

ip_bins = []
ip_bins.append(bin(int(octets[0])))
ip_bins.append(bin(int(octets[1])))
ip_bins.append(bin(int(octets[2])))
ip_bins.append(bin(int(octets[3])))

try:
    print("{:12}{:12}{:12}{:12}".format(*octets))
    print("{:12}{:12}{:12}{:12}".format(*ip_bins))
except IndexError:
    print("Not enough octets in your IP address, please try again.")

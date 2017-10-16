#!/usr/env/bin python
from __future__ import print_function

name1= 'Krishelle'
name2 = 'Nicole'
name3 = 'Hardson'

try:
    name4 = raw_input("Please enter the last part of your name: ")
except NameError:
    name4 = input("Please enter the last part of your name: ")

print("{:>30}{:>30}{:>30}{:>30}".format(name1, name2, name3, name4))

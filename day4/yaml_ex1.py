#!/usr/bin/env python

from __future__ import print_function
import yaml

def read_file(filename):
    with open(filename) as f:
        output = yaml.load(f)
    return output

def main():
    output = read_file('my_file2.yaml')
    print(output)

if __name__ == '__main__':
    main()

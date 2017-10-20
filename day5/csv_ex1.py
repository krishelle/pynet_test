#!/usr/bin/env python
from __future__ import print_function
import csv
import jinja2

def main():
    template_file = '/home/student13/pynet_test/day5/juniper_bgp.j2'
    with open(template_file) as f:
        bgp_template = f.read()

    template = jinja2.Template(bgp_template)

    csv_file = 'csv_ex1.csv'
    with open(csv_file) as f:
        csv_content = csv.DictReader(f) #this is how you read in a csv file, returns dict.
    
        for entry in csv_content:
            temp_entry = template.render(entry)
            print()
            print(temp_entry)
            print()

if __name__ == '__main__':
    main()

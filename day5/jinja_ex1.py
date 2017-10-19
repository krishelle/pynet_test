#!/usr/bin/env python
from __future__ import print_function
from jinja2 import Template

def main():
    try:
        with open("/home/student13/pynet_test/day5/juniper_bgp.j2") as f:
            template = f.read()
    except: 
        raise Exception

    variables = {
        "neighbor1": "10.100.1.7",
        "neighbor2": "10.100.99.1",
        "neighbor3": "10.100.8.1",
        "peer_as": 88,
    }
    
    template_obj = Template(template)
    try: 
        k = template_obj.render(variables)
        print(k)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()

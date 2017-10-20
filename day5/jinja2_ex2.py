#!/usr/bin/env python
from __future__ import print_function
import jinja2

my_vars = { 'intr_list': [
    ('ge-0/0/0', '10.10.10.1/24'),
    ('ge-0/0/1', '10.10.11.1/24'),
    ('ge-0/0/2', '10.10.12.1/24'),
    ('ge-0/0/3', '10.10.13.1/24'),
]
}

pre_template = """
interfaces {
{%- for intr, ip in intr_list %}
    {{ intr }} {
        unit 0 {
            replace:
            family inet{
                address 10.10.10.1/24;
            }
        }
    }
{%- endfor %}
"""


def main():
    template = jinja2.Template(pre_template)
    output = template.render(**my_vars)
    print(output)

if __name__ == '__main__':
    main()

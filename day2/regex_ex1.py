from __future__ import print_function
import re

with open('show_int_fa4.txt') as f:
    output = f.read()

packets = re.search(r'(\d+) packets input, (\d+) bytes', output, flags=re.M)
print(packets.group(0))
packets2 = re.search(r'(\d+) packets output, (\d+) bytes', output)

print('Packets input: {}, Packets output: {}'.format(packets.group(1), packets2.group(1)))
print('Bytes input: {}, Bytes output: {}'.format(packets.group(2), packets2.group(2)))

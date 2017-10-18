from __future__ import print_function

with open('show_version.txt') as f:
    output = f.read()

lines = output.splitlines()

for line in lines:
    if 'Processor board ID' in line:
        words = line.strip().split('Processor board ID ')
        sn = words[-1]

print('The Serial Number is: {}'.format(sn))

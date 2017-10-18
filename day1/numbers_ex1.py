#!usr/bin/env python

from __future__ import print_function

try: 
    num1 = int(raw_input('Enter first number: '))
    num2 = int(raw_input('Enter second number: '))
except NameError:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

print('Sum: {}'.format(num1 + num2))
print('Difference: {}'.format(num1 - num2))
print('Product: {}'.format(num1*num2))
print('Division: {}'.format(float(num1)/num2))


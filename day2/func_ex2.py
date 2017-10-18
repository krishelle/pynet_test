from __future__ import print_function

def my_func(x,y,z=20):
    try:
        sum = x + y + z
    except Exception as e:
        print(e)
    print(sum)

# Exercise 1
#my_func(10, 20, 30)
#my_func(19, 29)
#my_func(12, 10, z=10)
#my_func(12, y=10, z=10)
#my_func([12], y=[10], z=[10])

# Exercise 2
lst = [2 , 4 , 6]
my_func(*lst)
dct = { 'x': 5, 'y': 6, 'z':10}
my_func(**dct)

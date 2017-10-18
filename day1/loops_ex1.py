#!/usr/bin/env python
from __future__ import print_function

my_list = range(50)

for ele in my_list:
    if ele == 13:
        continue
    elif ele == 39:
        break
    print(ele)



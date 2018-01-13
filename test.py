#!/usr/bin/env python3
from functional_test import map_and_reduce

names = ['Mary', 'Isla', 'Sam']

new_names = map_and_reduce.functional(names)

for n in new_names:
    print(n)

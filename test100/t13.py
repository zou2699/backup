#!/usr/bin/env python
# encoding: utf-8

for n in range(100,1000):
    i = n / 100
    j = n % 100 / 10
    k = n % 100 % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        print n

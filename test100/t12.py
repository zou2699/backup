#!/usr/bin/env python
# encoding: utf-8

from math import sqrt
from sys import stdout

h = 0
leap = 1

for i in range(101,201):
    k = int(sqrt(i+1))
    for j in range(2,k+1):
        if i % j == 0:
            leap = 0
            break
    if leap == 1:
        print '%-4d' % i
        h += 1
        if h % 10 == 0:
             print ''
    leap = 1
print "The total is %d" % h



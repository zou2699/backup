#!/usr/bin/env python
# encoding: utf-8

a = int(raw_input("a =  "))
n = int(raw_input("n =  "))
Tn = 0
Sn = []
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn

Sn = reduce(lambda x,y : x + y,Sn)
print Sn

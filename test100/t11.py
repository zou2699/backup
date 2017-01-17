#!/usr/bin/env python
# encoding: utf-8

month = int(raw_input("Enter month:"))
f1 = 1
f2 = 1

if month <= 2:
    print "兔子有%d对" % f1
    exit()
else:
    for i in range(2,month):
        f1,f2 = f2,f1+f2
    print "兔子有%d对" % f2

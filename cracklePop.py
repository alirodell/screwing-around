#!/usr/bin/python

i = 1
while i <= 100:
    if i % 5 == 0 and i % 3 == 0:
        print "CracklePop"
    elif i % 5 == 0:
        print "Pop"
    elif i % 3 == 0:
        print "Crackle"
    else:
        print i
    i += 1

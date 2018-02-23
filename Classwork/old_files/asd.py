#!/usr/bin/python
import math
print "ax^2+bx+c"

def diskriminant(a,b,c):
 return b*b-4*a*c

a=input("nermutsel a: ")
b=input("nermutsel b: ")
c=input("nermutsel c: ")

if (a==0):
 if (b==0):
  print "lucum chuni"
 else: 
  print "x=",(-c/b)
else:
 if (diskriminant(a,b,c)<0):
  print "lucum chuni"
 else:
  print "x1=",((-b+math.sqrt(diskriminant(a,b,c)))/(2*a))
  print "x2=",((-b-math.sqrt(diskriminant(a,b,c)))/(2*a))




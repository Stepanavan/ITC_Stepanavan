#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import os

os.system('clear')

print "|֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊|"
print "|Քառակուսի գծի հավասարում a,b,c պարամետրերով|"
print "|֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊|"
print " "

while True:
	try:
		a = input("nermucel a֊ն ")
		b = input("nermucel b֊ն ")
		c = input("nermucel c֊ն ")
		break
	except (NameError,SyntaxError):
		os.system('clear')

		print "|֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊|"
		print "|Քառակուսի գծի հավասարում a,b,c պարամետրերով|"
		print "|֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊֊|"
		print " "
		print ("խնդրում ենք ներմուծել միայն թիվ")

os.system('clear')
print "****************************"
print "     a=",a , " b=", b ," c=", c
print "****************************"
print  "   {", a,'x^2 +',b,'x+',c,'= 0  }'
print "****************************"


def qarakusi(a,b,c): 
 D=b*b-4*a*c
 if a != 0: 
  if D >= 0:
   x1 = (-b-math.sqrt(D))/(2*a)
   x2 = (-b+math.sqrt(D))/(2*a)
   print "    x1= ", (x1)
   print "    x2= ", (x2) 
   print "****************************"
  elif D < 0:
   print "Հավասարումը լուծում չունի"
   print "****************************"
 else:
  if b != 0:
   x = (-c/b)
   print "     x= ", x
   print "****************************"
  else:
   print "Հավասարումը լուծում չունի"
   print "****************************"

qarakusi(a,b,c)


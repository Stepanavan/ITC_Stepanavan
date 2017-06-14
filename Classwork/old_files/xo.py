#!/usr/bi,n/python
import random
anun =[]
for i in range(11):
 #anun.append(input("ner ambo tiv:"))
 anun.append(random.randint(-10,100))

for i in range(11):
 print anun[i], "|",

print 

qanak=0

for i in range(10):
 if (anun[i]<=3 and anun[i+1]<0):
  print "anun[",i,"]=",anun[i]
  print "anun[",i+1,"]=",anun[i+1]
  print "i=",i
  qanak=qanak+1
if (qanak==0):
 print "chka"
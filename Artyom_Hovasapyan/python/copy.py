#!/usr/bin/python
import random
j=[]
gumar=0.0
qanak=0.0
gumar11=0.0
for i in range(10):
	j.append(random.randint(1,100))
for i in range(10):
	gumar11=gumar11+j[i]
	if j[i]%2==1:
		gumar=gumar+j[i]
		qanak=qanak+1

for i in range(10):
	print j[i]
	

print gumar/qanak
print qanak
print "amenamet",min(j)
print "amenapoqr",max(j)

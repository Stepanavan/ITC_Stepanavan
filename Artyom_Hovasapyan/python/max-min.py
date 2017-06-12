#!/usr/bin/python
min=0
max=0
togh=[]
for i in range(10):
	print "a[",i,"]=",
	a=input("")
	togh.append(a)
min=togh[0]
max=togh[0]
for i in range(10):
	if min>togh[i]:
		min=togh[i]
	if max<togh[i]:
		max=togh[i]
print "max=",max
print "min=",min

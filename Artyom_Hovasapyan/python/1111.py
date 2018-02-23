#!/usr/bin/python
import random
def numberstonumber(x):
	nums=list(str(x))
	temp=[]
	for i in nums:
		temp.append(int(i))
	return temp
for i in range(10):
	y=random.randint(0,10000)
summ=0
for i in numberstonumber(y):
	if (i%2==1):
		summ+=i
		print i
print "yndanur gumar=", summ
#for i in numberstonumber(y):
#	print i
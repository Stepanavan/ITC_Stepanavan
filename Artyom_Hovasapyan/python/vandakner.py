#!/usr/bin/python
togh=[]
S1=0
S2=0
S3=0
S4=0
for i in range(3):
	syun=[]
	for j in range(3):
		print "a[",i,",",j,"]=",
		a=input("")
		syun.append(a)
	togh.append(syun)

for i in range(3):
	for j in range(i,3):
		S1+=togh[i][j]
for i in range(3):
	for j in range(0,3-i):
		S2+=togh[i][j]
for i in range(3):
	for j in range(0,i+1):
		S3+=togh[i][j]
for i in range(3):
	for j in range(2-i,3):
		S4+=togh[i][j]
print "S1 =" ,S1
print "S2 =" ,S2
print "S3 =" ,S3
print "S4 =" ,S4

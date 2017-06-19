#!/usr/bin/python
# -*- coding: utf-8 -*-

minchev = 1+ input("ներուծեք ձեր թիվը  ")
togh = []
element = []
ayl_element = []
def factorial(x):
	if x==0 or x==1:
		return 1
	else:
		return x*factorial(x-1)
def zugordutiun(x,y):
	return factorial(x)/(factorial(x-y)*factorial(y))
def fibonachi(x):
	if x==1 or x==2:
		return 1
	else:
		return (fibonachi(x-1)+fibonachi(x-2))

for i in range(0,minchev):
	element = []	
	for j in range(0,(i+1)):
		element.append(zugordutiun(i,j))
	togh.append(element)

for i in range(1,minchev):
	ayl_element.append(fibonachi(i))

print"Պասկալի եռանկյունը  1֊ից մինչև "+ str(minchev-1)+" թիվը ունի հետևյալ տեսքը"
for i in range(1,minchev):
	print togh[i]
print "---------------------------"
print"Իսկ Ֆիբոնաչին 1֊ից մինչև "+ str(minchev-1)+" թիվը ունի հետևյալ տեսքը"

print ayl_element
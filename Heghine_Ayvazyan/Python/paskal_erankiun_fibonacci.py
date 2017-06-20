#!/usr/bin/python
# -*- coding: utf-8 -*-

minchev = 1+ input("Nermutcel tiv")
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

print"Paskali erankyun@ 1-ic minchev "+ str(minchev-1)+" tiv@ stacvec"
for i in range(1,minchev):
	print togh[i]
print "---------------------------"
print"Isk Fibonaccin 1-ic minchev "+ str(minchev-1)+" tiv@ stacvec "

print ayl_element

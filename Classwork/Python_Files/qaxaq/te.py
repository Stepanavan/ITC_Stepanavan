#!/usr/bin/python
# -*- coding: utf-8 -*-

def bajanarar(a,b):
	if a == b:
		return a
	else:
		if a > b:
			a = a - b
		if b > a:
			b = b - a
		return bajanarar(a,b)

def bazmapatik(a,b):
	return a*b/bajanarar(a,b)
		

def factorial(a):
	if a==1 or a==0:
		return 1
	else:
		return a*factorial(a-1)


def factorial1(a):
	k = 1
	if a == 0:
		return 1
	for i in range(1,a+1):
		k = k * i
	return k  



def paskali_tox(a):
	b=[]
	
		



print factorial(5)
print factorial1(5)




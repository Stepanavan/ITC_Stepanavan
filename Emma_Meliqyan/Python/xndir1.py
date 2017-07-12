#!/usr/bin/python3
import math



def parz(a):
	if a < 2:
		return False
	for i in range(2,int(math.sqrt(a))+1):
		if ((a % i) == 0):
			return False
	return True
		





			
for i in range(1,200):		 
	if parz(i) :
		print(i, "parz e")
	

	 





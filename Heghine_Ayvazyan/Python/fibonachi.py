#!/usr/bin/python
def fibonachi(i):
	
	  if i==1 or i==2 :
		return 1

	  else:
		return fibonachi(i-1)+fibonachi(i-2)
 
print fibonachi(12)
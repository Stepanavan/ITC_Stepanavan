#!/usr/bin/python
def f(a,b):
	if a==b:
		return a
	elif a > b: 
		a=a-b
	else:
		b=b-a
	return f(a,b)
def rec1(a,b):
	return a*b/f(a,b)

a1=int(raw_input("nermutel a-n:"))
b1=int(raw_input("nermutel b-n:"))
print f(a1,b1)
print rec1(a1,b1)


#factorial= orinak 5 faktorian = 4 faktorial...1faktoria bacarutyuna 0 faktorian = 1     
# 5 factorial=5*4*3*2*1
def factorial(a):
	if a==1 or a==0 :
		return 1
	else:
		return a*factorial(a-1)

print factorial(5)

# kamel
#def factorial1(a)
	#k=1
	#if a==0 :
		#return 1
	#for i in range (1,a+1):
		#k=k*i
	#return k 
#print factorial1(aystex texadrvat tvi)

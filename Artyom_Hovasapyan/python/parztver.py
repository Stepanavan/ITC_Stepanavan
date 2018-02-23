#!/usr/bin/python

#def isprime(n):
    #if n == 1:
     #   return False
    #for x in range(2, n):
   #     if n % x == 0:
   #         return False
  #      else:
 #           return True
#def primes(n = 1):
   # while(True):
  #      if isprime(n): yield n
 #       n += 1
#for n in primes():
 #   if n >100: break
#    print(n)

from math import sqrt
n = input("n=")
lst=[]
for i in xrange(2, n+1):
    for j in lst:
        if j > int((sqrt(i)) + 1):
            lst.append(i)
            break 
        if (i % j == 0):
            break
    else:
        lst.append(i)
print lst


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



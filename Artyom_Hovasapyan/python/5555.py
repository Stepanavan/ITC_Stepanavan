from math import sqrt
n=input("n=")
lst=[]

gumar11=0.0
qanak=0.0
gumar=0.0

	
for i in range(2, n+1):
    
    for j in lst:
	 
        if j > int((sqrt(i)) + 1):
	
          
  	 
	  lst.append(i)
	  
	  break 
	  
        if (i % j == 0):
			
        	break
    else:
        lst.append(i)
	
	
print lst
print  "qanak=",(len(lst))


print "amenapoqr=",(min(lst))
print "amenamet=",(max(lst))



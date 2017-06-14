def function(i,j):
 while (i>=1):
  i=i-1
  if ((i%j)==0):
   print (i)
 return
print ("Step Lib Products ...")
print ("Tiv Tur Bajanem")
try:
 function(i = int(raw_input("Tiv=: ")),j = int(raw_input("Inchi Bajanem: ")))
except ValueError:
 print "Krkin pordir"
else:
 print "All OK"


qanak=0
i = 2
while(i < 100):
 j = 2
 while(j <= (i/j)):
  if not(i%j): break
  j = j + 1
 if (j > i/j) :
  print i , " parz tiv e"
  qanak=qanak+1
 i = i + 1

print "qanak=",qanak
print "Good bye!"
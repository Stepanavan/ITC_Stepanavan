#!/usr/bin/python
ochinyan=[]
for i in range(1,10): 
 ochinyan.append(i)

def dasht():
 print "-------------"
 for j in range (9):
  print "|",ochinyan[j],
  if ((j+1)%3==0):
   print "|"
   print "-------------"
 return


def stugum(X_kam_O):
 if (ochinyan[0]==X_kam_O and ochinyan[1]==X_kam_O and ochinyan[2]==X_kam_O or
 ochinyan[3]==X_kam_O and ochinyan[4]==X_kam_O and ochinyan[5]==X_kam_O or \
 ochinyan[6]==X_kam_O and ochinyan[7]==X_kam_O and ochinyan[8]==X_kam_O or \
 ochinyan[0]==X_kam_O and ochinyan[3]==X_kam_O and ochinyan[6]==X_kam_O or \
 ochinyan[1]==X_kam_O and ochinyan[4]==X_kam_O and ochinyan[7]==X_kam_O or \
 ochinyan[2]==X_kam_O and ochinyan[5]==X_kam_O and ochinyan[8]==X_kam_O or \
 ochinyan[6]==X_kam_O and ochinyan[4]==X_kam_O and ochinyan[2]==X_kam_O or \
 ochinyan[0]==X_kam_O and ochinyan[4]==X_kam_O and ochinyan[8]==X_kam_O):
  return True
 return False


dasht()


for k in range(9):
 try:
  seghmir=int(raw_input("mutq ara dashti hamar@: "))
 except ValueError:
  print "1mutqagreq tiv"
  k=k-1
 else:
  while (seghmir < 1 or seghmir >9 or seghmir != ochinyan[seghmir-1]):
   try:
    seghmir=int(raw_input("sxal mutq, noric pordzir: "))
   except ValueError:
    print "2mutqagreq tiv"
  if (k%2==0):
   ochinyan[seghmir-1]="X"
   dasht()
   if (stugum("X")):
    print "Haxtec X"
    break

  if (k%2==1):
   ochinyan[seghmir-1]="O"
   dasht()
   if (stugum("O")):
    print "Haxtec O"
    break

  if (k==8):
   print "vochvoqi"

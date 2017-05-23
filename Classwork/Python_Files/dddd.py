#!/usr/bin/python
import os
import gc

ochinyan=[]
for i in range(1,10):
 ochinyan.append(i)

def dasht():

 xxx = open('temp', 'w')

 for j in 0,1,2:
  xxx.write("|"+str(ochinyan[(j)*3+0])+"|"+str(ochinyan[(j)*3+1])+"|"+str(ochinyan[(j)*3+2])+"|\n")

 xxx.close()
 gc.collect()
 f = open('temp','r')
 line = f.readline()
 os.system('clear')
 while line:
     print(line)
     line = f.readline()
 f.close()



def stugum(X_kam_O):
 if (ochinyan[0]==X_kam_O and ochinyan[1]==X_kam_O and ochinyan[2]==X_kam_O or
 ochinyan[3]==X_kam_O and ochinyan[4]==X_kam_O and ochinyan[5]==X_kam_O or
 ochinyan[6]==X_kam_O and ochinyan[7]==X_kam_O and ochinyan[8]==X_kam_O or
 ochinyan[0]==X_kam_O and ochinyan[3]==X_kam_O and ochinyan[6]==X_kam_O or
 ochinyan[1]==X_kam_O and ochinyan[4]==X_kam_O and ochinyan[7]==X_kam_O or
 ochinyan[2]==X_kam_O and ochinyan[5]==X_kam_O and ochinyan[8]==X_kam_O or
 ochinyan[6]==X_kam_O and ochinyan[4]==X_kam_O and ochinyan[2]==X_kam_O or
 ochinyan[0]==X_kam_O and ochinyan[4]==X_kam_O and ochinyan[8]==X_kam_O):
  return True
 return False


dasht()


for k in range(10):
 try:
  seghmir=int(input("mutq ara dashti hamar@: "))
 except ValueError:
  print ("1mutqagreq tiv")

 else:
  while (seghmir < 1 or seghmir >9 or seghmir != ochinyan[seghmir-1]):
   try:
    seghmir=int(input("sxal mutq, noric pordzir: "))
   except ValueError:
    print ("2mutqagreq tiv")
  if (k%2==0):
   ochinyan[seghmir-1]="X"
   dasht()
   if (stugum("X")):
    print ("Haxtec X")
    break

  if (k%2==1):
   ochinyan[seghmir-1]="O"
   dasht()
   if (stugum("O")):
    print ("Haxtec O")
    break

  if (k==8):
   print ("vochvoqi")

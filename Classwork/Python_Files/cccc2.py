#!/usr/bin/python
import os
ochinyan=[]
for i in range(1,10): 
 ochinyan.append(i)

def dasht():
 os.system('clear')
 print "-------------"
 for j in range (9):
  print "|",ochinyan[j],
  if ((j+1)%3==0):
   print "|"
   print "-------------"
 return

def stugum(X_kam_O):
 for i in range(3):
  if (ochinyan[3*i]==X_kam_O and ochinyan[3*i+1]==X_kam_O and ochinyan[3*i+2]==X_kam_O or
  ochinyan[i]==X_kam_O and ochinyan[i+3]==X_kam_O and ochinyan[i+6]==X_kam_O or \
  ochinyan[6]==X_kam_O and ochinyan[4]==X_kam_O and ochinyan[2]==X_kam_O or \
  ochinyan[0]==X_kam_O and ochinyan[4]==X_kam_O and ochinyan[8]==X_kam_O):
   return True
 return False

dasht()
k=0

while True:
 try:
  seghmir=int(raw_input("mutq areq dashti hamar@: "))
 except ValueError:
  dasht()
  print "duq mutqagrel eq simvol, mutqagreq tiv 1-9 sahmanum "
 else:
  while (seghmir < 1 or seghmir >9 or seghmir != ochinyan[seghmir-1]):
   try:
    dasht()
    seghmir=int(raw_input("zbaxvats dasht kam sxal tiv, mutqagreq mek ayl tiv 1-9 sahmanum: "))
   except ValueError:
    print "duq mutqagrel eq simvol, mutqagreq tiv 1-9 sahmanum"
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
   break

  k+=1
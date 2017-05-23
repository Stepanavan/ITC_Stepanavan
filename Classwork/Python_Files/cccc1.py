#!/usr/bin/python
import os
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
P  = '\033[35m' # purple

darak=[]
for i in range(9):
 darak.append(i+1)

def stugum(b):
 if (darak[0]==b and darak[3]==b and darak[6]==b or \
 darak[1]==b and darak[4]==b and darak[7]==b or \
 darak[2]==b and darak[5]==b and darak[8]==b or \
 darak[0]==b and darak[1]==b and darak[2]==b or \
 darak[3]==b and darak[4]==b and darak[5]==b or \
 darak[6]==b and darak[7]==b and darak[8]==b or \
 darak[0]==b and darak[4]==b and darak[8]==b or \
 darak[6]==b and darak[4]==b and darak[2]==b):
  print "haxtec: ", b
 return

def aaaaaa():
 print "-------------------"

 for i in range(9):
  print "|",O,darak[i],W,
  if ((i+1)%3==0):
   print "|"
   print "-------------------"
 return

os.system('clear')
aaaaaa()
for i in range(9):
 b=input("nermutsel dashti hamar@: ")
 if (i%2==0):
  darak[b-1]="X"
  stugum("X")
 if (i%2==1):
  darak[b-1]="O"
  stugum("O")
 os.system('clear')
 aaaaaa()


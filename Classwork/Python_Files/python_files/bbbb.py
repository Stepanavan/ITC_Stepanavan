#!/usr/bin/python
import os
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
P  = '\033[35m' # purple

def cin(tiv):
 print W
 while (tiv !=mapp[(tiv-1)]):
  B = input("Neemutseq dashti hamar@: ")
  tiv = B
 return B

def dasht():
 print R+'----------------'
 for i in range (3):
  print R+'|',W,mapp[(i*3+0)] ,R+'|',W,mapp[(i*3+1)] ,R+'|',W,mapp[(i*3+2)] ,R+'|'
  print R+'----------------'
 print W
 return

def stugum(A,B,C):
 for i in range(3):
  if ((mapp[(i*3+0)]==A and mapp[(i*3+1)]==A and mapp[(i*3+2)]==A) or \
  (mapp[(i)] == A and  mapp[(i+3)] == A and  mapp[(i+6)] ==A) or \
  (mapp[(0)] == A and  mapp[(4)] == A and  mapp[(8)] ==A) or \
  (mapp[(2)] == A and  mapp[(4)] == A and  mapp[(6)] ==A)):
   win_and_exit(B,C)
  else:
   continue

def win_and_exit(B,C):
 os.system('clear')
 print "Good Game",B,"Wins in " ,C+1,"step"
 dasht()
 exit()

def playing(A,B,C,D):
 os.system('clear')
 print "player ",A,"with  -",D,"-", C+1, "Step"
 dasht()
 B=cin(B)
 mapp[(B-1)]=D

B=-1
mapp=[]
for i in range(9):
 mapp.append(i+1)

os.system('clear')
print "******game started*****"
name1 = raw_input("-X-player Name ?: ")
name2 = raw_input("-0-player Name ?: ")
os.system('clear')

for j in range(9):
 pl=(j%2)
 if (pl==0):
  playing(name1,B,j,'X')
 if(pl==1):
  playing(name2,B,j,'0')

 if (j>4):
  stugum("X", name1 , j )
  stugum("0", name2 , j )

 if (j==8):
  os.system('clear')
  print "**********"
  print "**standoff**"
  print "***********"
  dasht()

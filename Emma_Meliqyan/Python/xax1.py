#!/usr/bin/python
import os
def cin(tiv):
 while (tiv !=mapp[(tiv-1)]):
  try:
   B = input("Neemutseq dashti hamar@: ")
  except NameError:
   print "katarel eq sxal mutq"
  else:
   tiv = B
   return B

def dasht():
 print "-------------"
 for i in range (3):
  print "|",mapp[(i*3+0)],"|",mapp[(i*3+1)],"|",mapp[(i*3+2)],"|"
  print "-------------"
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
 return

def win_and_exit(B,C):
 os.system('clear')
 print "Good Game",B,"Wins in " ,C+1,"step"
 dasht()
 exit()
 return

def playing(A,B,C,D):
 os.system('clear')
 print "player ",A,"with  -",D,"-", C+1, "Step"
 dasht()
 B=cin(B)
 mapp[(B-1)]=D
 return

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

 if (j>=4):
  stugum("X", name1 , j )
  stugum("0", name2 , j )

 if (j==8):
  os.system('clear')
  print "**********"
  print "**standoff**"
  print "***********"
  dasht()

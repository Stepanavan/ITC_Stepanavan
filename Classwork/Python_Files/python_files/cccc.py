#!/usr/bin/python
import os
def cin(tiv):
 while (tiv !=mapp[(tiv-1)]):
  B = input("Neemutseq dashti hamar@: ")
  tiv = B
 return B

def dasht():
 print "-------------"
 for i in range (3):
  print "|",mapp[(i*3+0)],"|",mapp[(i*3+1)],"|",mapp[(i*3+2)],"|"
  print "-------------"
 return

def stugum(x_kam_o):
 for i in range(3):
  if ((mapp[(i*3+0)]==x_kam_o and mapp[(i*3+1)]==x_kam_o and mapp[(i*3+2)]==x_kam_o) or \
  (mapp[(i)] == x_kam_o and  mapp[(i+3)] == x_kam_o and  mapp[(i+6)] ==x_kam_o) or \
  (mapp[(0)] == x_kam_o and  mapp[(4)] == x_kam_o and  mapp[(8)] ==x_kam_o) or \
  (mapp[(2)] == x_kam_o and  mapp[(4)] == x_kam_o and  mapp[(6)] ==x_kam_o)):
   return 1
  else:
   continue
 return 0

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
  if (stugum("X")==1):
   win_and_exit(name1,j)
  if (stugum("0")==1):
   win_and_exit(name2,j)
  

 if (j==8):
  os.system('clear')
  print "**********"
  print "**standoff**"
  print "***********"
  dasht()

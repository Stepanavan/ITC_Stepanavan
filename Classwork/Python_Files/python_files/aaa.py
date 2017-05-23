#!/usr/bin/python
import os
import string

def cin(tiv):
 B=-1
 while ( tiv != mapp[(tiv-1)]):
  B = input('Nermutseq dashti hamar@ ')
  tiv=B
 return B

def dasht():
 for i in range(3):
  print "-------------"
  print  "|",mapp[(i*3+0)],"|",mapp[(i*3+1)],"|", mapp[(i*3+2)],"|"
 print "-------------"
 return

def stugum(A,B,C):
 for i in range(3):
  if (mapp[(i*3+0)] == A and mapp[(i*3+1)] == A and mapp[(i*3+2)] == A):
   os.system('clear')
   print "Good Game",B,"Wins in ",C,"Step"
   exit()
  elif (mapp[i] == A and mapp[(i+3)] == A and mapp[(i+6)] == A):
   os.system('clear')
   print "Good Game",B,"Wins in ",C,"Step"
   exit()
  elif (mapp[0] == A and mapp[4] == A and mapp[8] == A):
   os.system('clear')
   print "Good Game",B,"Wins in ",C,"Step"
   exit()
  elif (mapp[2] == A and mapp[4] == A and mapp[6] == A):
   os.system('clear')
   print "Good Game",B,"Wins in ",C,"Step"
   exit()
  else:
   continue

os.system('clear')
print "*****GAME STARTED*****"
name1 = raw_input(" nermucel X-ov xaxacoxi anuny ")
name2 = raw_input(" nermucel O-ov xaxacoxi anuny ")

os.system('clear')

B=-1
mapp = []
for i in range(9):
 mapp.append(i+1)

for j in range(9):
 pl=(j%2)
 if (pl==0):
  os.system('clear')
  print "____________________________________ "
  print "                                     "
  print "Player ",name1," with -X-" ,j,  "Step"
  print "____________________________________ "
  dasht()
  B=cin(B)
  mapp[(B-1)]="X"
 if (pl==1):
  os.system('clear')
  print "____________________________________ "
  print "                                     "
  print "Player ",name2," with -O- ",j,  "Step"
  print "____________________________________ "
  dasht()
  B=cin(B)
  mapp[(B-1)]="O" 
 if (j>4):
  stugum("X", name1,j)
  stugum("O", name2,j)
 if (j==8):
  os.system('clear')
  print "*********************************"
  print "            Standoff             "
  print "*********************************"
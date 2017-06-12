#!/usr/bin/python
import os

def k_to_file_tmp(k):
 aaaa = open('tmp','w')
 aaaa.write(str(k))
 aaaa.close()

def read_k_from_tmp():
 aaaa = open('tmp','r')
 k = int(aaaa.read())
 aaaa.close()
 return k

def datark_xo_fayl():
 aaaa = open('xo','w')
 aaaa.close()

def ochinyan_to_file_xo(bbb):
 aaaa = open('xo','w')
 for i in range(9):
  aaaa.write(str(bbb[i]))
 aaaa.close()

def read_and_print_file_xo():
 aaaa = open('xo','r')
 for i in range(9):
  ochinyan[i] = str(aaaa.read(1))
 aaaa.close()

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


ochinyan=[]
for i in range(1,10): 
 ochinyan.append(i)
read_and_print_file_xo()


dasht()


k=0
k=read_k_from_tmp()

while True:
 k=read_k_from_tmp()
 try:
  read_and_print_file_xo()
  k=read_k_from_tmp()
  seghmir=int(raw_input("mutq areq dashti hamar@: "))
 except ValueError:
  dasht()
  print "duq mutqagrel eq simvol, mutqagreq tiv 1-9 sahmanum "
 else:
  print seghmir
  while (seghmir < 1 or seghmir >9 or str (seghmir) != str(ochinyan[seghmir-1])):
   try:
    dasht()
    read_and_print_file_xo()
    k=read_k_from_tmp()
    seghmir=int(raw_input("zbaxvats dasht kam sxal tiv, mutqagreq mek ayl tiv 1-9 sahmanum: "))
   except ValueError:
    print "duq mutqagrel eq simvol, mutqagreq tiv 1-9 sahmanum"
  if (k%2==0):
   ochinyan[seghmir-1]='X'
   ochinyan_to_file_xo(ochinyan)
   read_and_print_file_xo()
   dasht()
   if (stugum('X')):
    print "Haxtec X"
    break

  if (k%2==1):
   ochinyan[seghmir-1]='O'
   ochinyan_to_file_xo(ochinyan)
   read_and_print_file_xo()
   dasht()
   if (stugum('O')):
    print "Haxtec O"
    break

  if (k==8):
   print "vochvoqi"
   break

  k+=1
  k_to_file_tmp(k)

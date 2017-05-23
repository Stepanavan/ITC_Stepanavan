#!/usr/bin/python
import os

ochinyan=[]
for i in range(1,10): 
 ochinyan.append(i)

def datark_xo_fayl():
 aaaa = open('xo','w')
 aaaa.close()

def ochinyan_to_file_xo(bbb):
 aaaa = open('xo','w')
 for i in bbb:
  aaaa.write(str(i))
 aaaa.close()

def read_and_print_file_xo():
 aaaa = open('xo','r')
 for i in range(9):
  ochinyan[i] = aaaa.read(1)
 aaaa.close()

b=input("nermutsel dashti hamar@: ")
ochinyan[b-1]='x'

datark_xo_fayl()
ochinyan_to_file_xo(ochinyan)
read_and_print_file_xo()

for i in range(9):
 print ochinyan[i],
print

for i in range(9):
 print ochinyan[i],
print

for i in range(9):
 print ochinyan[i],
print

ochinyan_to_file_xo(ochinyan)

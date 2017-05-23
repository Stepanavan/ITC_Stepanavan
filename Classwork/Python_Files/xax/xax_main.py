#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

#patrastel datark masiv ev lracnel 1-ic 9-@ tver@
och=[]
def sarqel():
 for i in range(1,10):
  och.append(str(i))
 return

def sarqel2():
 aaaa=open("xo","r")
 for i in range(9):
  och.append(str(aaaa.read(1)))
 aaaa.close()
 return

#dasht nkarox funkcia
def dasht():
 print "-------------"
 for i in range(9):
  print "|",och[i],
  if (i+1)%3==0:
   print "|"
   print "-------------"
 return

#dashti arjeqner@ "xo" fayli mej grox funkcia
def och_to_file_xo():
 aaaa=open("xo","w")
 for i in range(9):
  aaaa.write(str(och[i]))
 aaaa.close()
 return

#"xo" faylic kardacox ev och masivi mej lcnox funkcia
def read_xo_to_och():
 aaaa=open("xo","r")
 for i in range(9):
  och[i]=aaaa.read(1)
 aaaa.close()
 return

#voroshum e qayl@, aysinqn x-n e xaxalu, te o-n(kenti depqum - x, zuygi depqum -o)
def qayl():
 read_xo_to_och()
 k=0
 for i in range(9):
  if str(i+1)==och[i]:
   k=k+1
 return (10-k)


def stugum(X_kam_O): # Հաղթանակը ստուգող ֆունկցիան
 read_xo_to_och()
 for i in range(3):
  if (och[3*i]==X_kam_O and och[3*i+1]==X_kam_O and och[3*i+2]==X_kam_O or
  och[i]==X_kam_O and och[i+3]==X_kam_O and och[i+6]==X_kam_O or \
  och[6]==X_kam_O and och[4]==X_kam_O and och[2]==X_kam_O or \
  och[0]==X_kam_O and och[4]==X_kam_O and och[8]==X_kam_O):
   return True
 return False

def refresh():
 read_xo_to_och()
 dasht()
 os.system('sleep 0.5')
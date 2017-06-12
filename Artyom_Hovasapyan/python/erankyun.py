#!/usr/bin/python
# -*- coding: utf-8 -*-
import math


class ket:
 x=0
 y=0

class erankyun:
 A=ket()
 B=ket()
 C=ket()
 def a(self):
  self.A.x=float(raw_input("Մուտքագրեք A կետի x֊ը:"))
  self.A.y=float(raw_input("Մուտքագրեք A կետի y֊ը:"))
  print "A(",self.A.x,",",self.A.y,")"
  return
 def b(self):
  self.B.x=float(raw_input("Մուտքագրեք B կետի x֊ը:"))
  self.B.y=float(raw_input("Մուտքագրեք B կետի x֊ը:"))
  print "B(",self.B.x,",",self.B.y,")"
  return
 def c(self):
  self.C.x=float(raw_input("Մուտքագրեք C կետի x֊ը:"))
  self.C.y=float(raw_input("Մուտքագրեք C կետի x֊ը:"))
  print "C(",self.C.x,",",self.C.y,")"
  return
 def a_koxmi_erkarutyun(self):
  erk=math.sqrt( (self.A.x-self.B.x)*(self.A.x-self.B.x)+(self.A.y-self.B.y)*(self.A.y-self.B.y) )
  return erk
 def b_koxmi_erkarutyun(self):
  erk=math.sqrt( (self.C.x-self.B.x)*(self.C.x-self.B.x)+(self.C.y-self.B.y)*(self.C.y-self.B.y) )
  return erk
 def c_koxmi_erkarutyun(self):
  erk=math.sqrt( (self.A.x-self.C.x)*(self.A.x-self.C.x)+(self.A.y-self.C.y)*(self.A.y-self.C.y) )
  return erk
 def paragits(self):
  p=self.a_koxmi_erkarutyun()+self.b_koxmi_erkarutyun()+self.c_koxmi_erkarutyun()
  return p
 def mak(self):
  s=math.sqrt( self.paragits()/2*(self.paragits()/2-self.a_koxmi_erkarutyun())*(self.paragits()/2-self.b_koxmi_erkarutyun())*(self.paragits()/2-self.c_koxmi_erkarutyun()) )
  return s




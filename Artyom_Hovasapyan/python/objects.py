#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def erkarutyun(a,b):
	return math.sqrt( (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y) )

class ket:
	def __init__(self, x , y):
		self.x = x
		self.y = y

class erankyun():
	A=ket(0.0,0.0)
	B=ket(0.0,0.0)
	C=ket(0.0,0.0)
	def __init__(self, a, b, c):
		self.A.x=a.x
		self.A.y=a.y
		self.B.x=b.x
		self.B.y=b.y
		self.C.x=c.x
		self.C.y=c.y
		self.paragits = erkarutyun(self.A,self.B)+erkarutyun(self.A,self.C)+erkarutyun(self.B,self.C)
		self.makeres = math.sqrt((self.paragits/2)*(self.paragits/2-erkarutyun(self.A,self.B))*(self.paragits/2-erkarutyun(self.A,self.C))*(self.paragits/2-erkarutyun(self.C,self.B)))

class uxix():
	A=ket(0.0,0.0)
	B=ket(0.0,0.0)
	def __init__(self, a, b):
		self.A.x=a.x
		self.A.y=a.y
		self.B.x=b.x
		self.B.y=b.y
		self.k=((self.B.y-self.A.y)/(self.B.x-self.A.x))
		self.b=self.A.y-self.k*self.A.x

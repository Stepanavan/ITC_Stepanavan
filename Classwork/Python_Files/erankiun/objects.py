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
	Or=ket(0.0,0.0)
	OR=ket(0.0,0.0)
	def __init__(self, a=A, b=B, c=C):
		self.A.x=a.x
		self.A.y=a.y
		self.B.x=b.x
		self.B.y=b.y
		self.C.x=c.x
		self.C.y=c.y
		self.paragits = erkarutyun(self.A,self.B)+erkarutyun(self.A,self.C)+erkarutyun(self.B,self.C)
		self.makeres = math.sqrt((self.paragits/2)*(self.paragits/2-erkarutyun(self.A,self.B))*(self.paragits/2-erkarutyun(self.A,self.C))*(self.paragits/2-erkarutyun(self.C,self.B)))
		self.r=2*self.makeres/self.paragits
		self.R=erkarutyun(self.A,self.B)*erkarutyun(self.A,self.C)*erkarutyun(self.B,self.C)/(4*self.makeres)
		self.Or.x=(erkarutyun(self.A,self.B)*self.C.x+erkarutyun(self.A,self.C)*self.B.x+erkarutyun(self.B,self.C)*self.A.x)/self.paragits
		self.Or.y=(erkarutyun(self.A,self.B)*self.C.y+erkarutyun(self.A,self.C)*self.B.y+erkarutyun(self.B,self.C)*self.A.y)/self.paragits
		self.d=2*(self.A.x*(self.B.y-self.C.y)+self.B.x*(self.C.y-self.A.y)+self.C.x*(self.A.y-self.B.y))
		self.OR.x=((self.A.x*self.A.x+self.A.y*self.A.y)*(self.B.y-self.C.y)+(self.B.x*self.B.x+self.B.y*self.B.y)*(self.C.y-self.A.y)+(self.C.x*self.C.x+self.C.y*self.C.y)*(self.A.y-self.B.y))/self.d
		self.OR.y=((self.A.x*self.A.x+self.A.y*self.A.y)*(self.C.x-self.B.x)+(self.B.x*self.B.x+self.B.y*self.B.y)*(self.A.x-self.C.x)+(self.C.x*self.C.x+self.C.y*self.C.y)*(self.B.x-self.A.x))/self.d


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

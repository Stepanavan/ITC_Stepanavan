#!/usr/bin/python
# -*- coding: utf-8 -*-

class Ket():
	#Կետ կլասս, որն ունի x,y կոորդինատներ
	def __init__(self,a,b):
		#a֊ն դրից եկող 
		self.x=a
		self.y=b



class Erankyun(Ket):
	#Եռանկյուն կլասս, որն ունի 3 կետ, որոնք ժառանգել է Ket() կլասսից
	A=Ket(0,0)
	B=Ket(0,0)
	C=Ket(0,0)
	def __init__(self,a,b,c):
		self.A.x=a.x
		self.A.y=a.y
		self.B.x=b.x
		self.B.y=b.y
		self.C.x=c.x
		self.C.y=c.y


class qarankyun(Ket):
	A=Ket(0,0)
	B=Ket(0,0)
	C=Ket(0,0)
	D=Ket(0,0)
	def __init__(self,a,b,c,d):
		self.A.x=a.x
		self.A.y=a.y
		self.B.x=b.x
		self.B.y=b.y
		self.C.x=c.x
		self.C.y=c.y	
		self.D.x=d.x
		self.D.y=d.y




ss=Ket(0,0)
dd=Ket(10,0)
ff=Ket(0,10)
vv=Ket(10,10)
abc=Erankyun(ss,dd,ff)
print abc.A.x
qarak=qarankyun(ss,dd,ff,vv)
print qarak.D.y

class shrjan(Ket):
	O=Ket(0,0)
	def __init__(self,k,r):
		self.O=k
		self.r=r

aaaaa=shrjan(vv,100)
print aaaaa.O.x
bbbbbb=shrjan(100,100)
print bbbbbb.O.x



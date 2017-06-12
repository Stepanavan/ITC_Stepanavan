#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import *

class Ket:
	def __init__(self,x,y):
		self.__x=x
		self.__y=y

	def poxel(self,x,y):
		self.__x=x
		self.__y=y

	def tur_koordinatnets(self):
		return str(self.__x)+ " " +str(self.__y)
	def tur_x(self):
		return self.__x
	def tur_y(self):
		return self.__y
	def pttel(self,alfa):
		x1=self.__x * cos(alfa) + self.__y * sin(alfa)
		y1=self.__y * cos(alfa) - self.__x * sin(alfa)
		self.__x=x1
		self.__y=y1
	def pttel_xoyo_keti_nkatmamb(self,alfa,x0y0):
		x1=(self.__x-x0y0.tur_x()) * cos(alfa) + (self.__y-x0y0.tur_y()) * sin(alfa)
		y1=(self.__y-x0y0.tur_y()) * cos(alfa) - (self.__x-x0y0.tur_x()) * sin(alfa)
		self.__x=x1+x0y0.tur_x()
		self.__y=y1+x0y0.tur_y()

class Erankyun(Ket):
	A=Ket(0,0)
	B=Ket(0,0)
	C=Ket(0,0)
	def __init__(self,a,b,c):
		self.A=a
		self.B=b
		self.C=c
		self.__alfa=0

	def pttel_erankiun(self,alfa):
		self.__alfa=alfa
		self.A.pttel(alfa)
		self.B.pttel(alfa)
		self.C.pttel(alfa)
	def tpel_alfa(self):
		return self.__alfa
	def pttel_erankiun_keti_nkatmamb(self,alfa,x0y0):
		self.A.pttel_xoyo_keti_nkatmamb(alfa,x0y0)
		self.B.pttel_xoyo_keti_nkatmamb(alfa,x0y0)
		self.C.pttel_xoyo_keti_nkatmamb(alfa,x0y0)

hh=Ket(10,20)
vv=Ket(0,0)
gg=Ket(0,20)

ABC=Erankyun(hh,vv,gg)

print hh.tur_koordinatnets()
print ABC.tpel_alfa()
ABC.pttel_erankiun_keti_nkatmamb(30,hh)

print ABC.A.tur_koordinatnets()
print ABC.B.tur_koordinatnets()
print ABC.C.tur_koordinatnets()


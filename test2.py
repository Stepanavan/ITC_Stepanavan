#!/usr/bin/python
# -*- coding: utf-8 -*-
class Ket():
	def __init__(self,x=10,y=10):
		self.x=x
		self.__y=y

	def tpel_koordinatners(self):
		print self.x, self.__y

	def __del__(self):
		print "Ես ջնջվեցի"
A=Ket()
A.tpel_koordinatners()
B=Ket(50,50)
B.tpel_koordinatners()
A=Ket(30,30)
A.__y = 50
A.x = 20
A.tpel_koordinatners()
A.tpel_koordinatners()
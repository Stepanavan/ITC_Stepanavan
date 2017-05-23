#!/usr/bin/python
# -*- coding: utf-8 -*-

class Hasce():
	def __init__(self,anun,hamar):
		print "Ես աշխատեցի1"
		self.__poxoci_anun=anun
		self.__hamar=hamar
	def __del__(self):
		print "Ես աշխատեցի2"
	def tur_poxoci_anun(self):
		return self.__poxoci_anun
	def tur_hamar(self):
		return self.__hamar



aaaaa=Hasce("Sos Sargsyan", 70)
print aaaaa.__poxoci_anun
print aaaaa.tur_poxoci_anun()
print aaaaa.tur_hamar()
print "barev"





#!/usr/bin/python
# -*- coding: utf-8 -*-

class Hasce():
	def __init__(self,anun,hamar):
		print "Ես աշխատեցի1"
		self.poxoci_anun=anun
		self.hamar=hamar
	def __del__(self):
		print "Ես աշխատեցի2"


aaaaa=Hasce("Sos Sargsyan", 70)
print aaaaa.poxoci_anun
print aaaaa.hamar
print "barev"





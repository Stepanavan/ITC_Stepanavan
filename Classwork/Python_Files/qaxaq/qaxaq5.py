#!/usr/bin/python
# -*- coding: utf-8 -*-
class senyak ():
	def __init__ (self):
		self.hamar=raw_input("Ներմուծել սենյակի համարը ֊ ")
	def tpel_senyaki_hamar(self):
		print "Ես ", self.hamar, " համարի սենյակն եմ"
class hark (senyak):
	senyakner=[]
        
	def __init__ (self):
		self.hark=raw_input("Ներմուծել հարկի համարը ֊ ")
	def avelacnel_senyak(self,s):
		self.senyakner.append(s)
	def tpel_im_senyaknery(self):
		for i in self.senyakner:
			i.tpel_senyaki_hamar()


a=senyak()
b=senyak()

hark1=hark()
hark1.avelacnel_senyak(a)
hark1.avelacnel_senyak(b)
hark1.tpel_im_senyaknery()
print hark1.hark
print hark1.senyakner[0].hamar
hark1.senyakner[0].tpel_senyaki_hamar()





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
		self.senyakner=[]
	def avelacnel_senyak(self,s):
		if len(self.senyakner)<5:
			self.senyakner.append(s)
	def tpel_im_senyaknery(self):
		for i in self.senyakner:
			i.tpel_senyaki_hamar()
	def harki_senyakneri_qanak(self):
		return len(self.senyakner)

class shenq (hark):
	harker=[]
	def __init__ (self):
		self.hark=raw_input("Ներմուծել շենքի անունը ֊ ")
		self.harker=[]
	def avelacnel_senyak_senqin(self,s):
		if len(self.harker)==0:
			new_hark=hark()
			new_hark.avelacnel_senyak(s)
			self.harker.append(new_hark)
		elif self.harker[len(self.harker)-1].harki_senyakneri_qanak()<5:
			self.harker[len(self.harker)-1].avelacnel_senyak(s)
		else:
			new_hark=hark()
			new_hark.avelacnel_senyak(s)
			self.harker.append(new_hark)

	def tpel_im_harkery_senyaknerov(self):
		for i in self.harker:
			print "Ես ", i.hark, "հարկն եմ, ունեմ հետևյալ սենյակները" 
			i.tpel_im_senyaknery()
			print "――――――――――――――――――――――――――――――――――――――――――――――――――"
			
		
		
	

a=senyak()
b=senyak()
c=senyak()
d=senyak()
e=senyak()
f=senyak()


nor_shenq=shenq()
nor_shenq.avelacnel_senyak_senqin(a)
nor_shenq.avelacnel_senyak_senqin(b)
nor_shenq.avelacnel_senyak_senqin(c)
nor_shenq.avelacnel_senyak_senqin(d)
nor_shenq.avelacnel_senyak_senqin(e)
nor_shenq.avelacnel_senyak_senqin(f)



nor_shenq.tpel_im_harkery_senyaknerov()

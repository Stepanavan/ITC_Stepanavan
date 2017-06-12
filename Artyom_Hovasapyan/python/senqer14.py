#!/usr/bin/python
# -*- coding: utf-8 -*-


class senyak ():
       	def __init__ (self):
		self.hamar=raw_input("Ներմուծել սենյակի համարը ֊ ")
	def tpel_senyaki_hamar(self):
		print "Ես ", self.hamar, " համարի սենյակն եմ"
class hark (senyak):
	senyakner=[]
	qanak=1
	def __init__ (self,k=1):
		self.hark=raw_input("Ներմուծել հարկի համարը ֊ ")
		self.senyakner=[]
		self.qanak=k
	def avelacnel_senyak(self,s):
		if len(self.senyakner)<self.qanak:
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
			new_hark=hark(int(raw_input("Ներմուծել հարկի սենյակների քանակը ")))
			new_hark.avelacnel_senyak(s)
			self.harker.append(new_hark)
		elif self.harker[len(self.harker)-1].harki_senyakneri_qanak()<self.harker[len(self.harker)-1].qanak:
			self.harker[len(self.harker)-1].avelacnel_senyak(s)
		else:
			new_hark=hark(int(raw_input("Ներմուծել հարկի սենյակների քանակը ")))
			new_hark.avelacnel_senyak(s)
			self.harker.append(new_hark)

	def tpel_im_harkery_senyaknerov(self):
		for i in self.harker:
			print "Ես ", i.hark, "հարկն եմ, ունեմ հետևյալ սենյակները" 
			i.tpel_im_senyaknery()
			print "――――――――――――――――――――――――――――――――――――――――――――――――――"
			
class poxoc (shenq):
	shenqer=[]
	def __init__(self,shenq,hark,hamar):
		self.shenq=raw_input("shenqi anun")
		self.shenqer=[]
	def avelacnel__senqin_poxoc(self,u):
		if len(self.shenq)==0:
			new_poxoc=poxoc(int(raw_input("avelacnel poxoci hamar@ ")))
			new_poxoc.avelacnel_shenq(s)
		elif self.poxoc[len(self.poxoc)-1].shenq_eri_qanak()<self.shenq[len(self.shenq)-1].qanak:
			self.shenq[len(self.shenq)-1].avelacnel_shenq(s)
		else:
			new_poxoc=poxoc(int(raw_input("Ներմուծել poxoci anun")))
			new_poxoc.avelacnel_shenq(s)
			self.poxoc.append(new_shenq)

	def tpel_im_harkery_senyaknerov(self):
		for i in self.poxoc:
			print "Ես ", i.poxoc, "poxoc, ունեմ հետևյալ shenqer@" 
			i.tpel_im_poxoc()
			
			
		
	


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






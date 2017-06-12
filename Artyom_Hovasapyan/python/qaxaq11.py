#!/usr/bin/python
# -*- coding: utf-8 -*-

class Hasce():
	def __init__(self, anun, hamar):
		self.__poxoci_anun=anun
		self.__hamar=hamar
		return

	def tur_hasce(self):
		return self.__poxoci_anun + " "+ str(self.__hamar)

	def tur_poxoc(self):
		return self.__poxoci_anun

	def tur_hamar(self):
		return self.__hamar

	def veragri_hasce(self,poxoci_anun,hamar):
		self.__poxoci_anun=poxoci_anun
		self.__hamar=hamar
		
class Shenq(Hasce):
	def __init__(self,shqamutqer, harker,bnakaranner, hasce):
		self.__shqamutqer=shqamutqer
		self.__harker= harker
		self.__bnakaranner=bnakaranner
		self.veragri_hasce(hasce.tur_poxoc(),hasce.tur_hamar())
		
	def tur_tvyalners(self):
		return str(self.__shqamutqer)+" "+str(self.__harker)+" "+str(self.__bnakaranner)

	def tur_sqamutqer(self):
		return self.__shqamutqer

	def tur_harker(self):
		return self.__harker

	def tur_bnakaranner(self):
		return self.__bnakaranner

class Qaxaq():
	n = []
	def avelacnel_shenq(self,shenq):
		self.n.append(shenq)
		return
		
	def tpel_shenqeris_cucak(self):
		for i in self.n:
			print i.tur_hasce(),i.tur_bnakaranner()
		
	def pntrel_yst_bnakaranneri(self,qanak):
		print qanak, "բնակարան ունեցող շենքերի ցուցակ"
		for i in self.n:
			if i.tur_bnakaranner()==qanak:
				print i.tur_hasce(),i.tur_bnakaranner()

	def grel_fayli_mej(self,a):
		aaaa=open(a,"w")
 		for i in self.n:
			aaaa.write(i.tur_hasce()+" " +i.tur_tvyalners())
			aaaa.write("\n")
		aaaa.close()
		return
	def poxel_poxoci_anuny(self, him_anun,nor_anun):
		for i in self.n:
			if i.tur_poxoc()==him_anun:
				i.veragri_hasce(nor_anun,i.tur_hamar())
                	

qaxaq=Qaxaq()
hasce=Hasce("Sos Sargsyan", 70)
A=Shenq(3,5,40,hasce)
qaxaq.avelacnel_shenq(A)
hasce=Hasce("Sos Sargsyan", 71)
A=Shenq(3,5,50,hasce)
qaxaq.avelacnel_shenq(A)
hasce=Hasce("Moskovyan", 72)
A=Shenq(3,5,40,hasce)
qaxaq.avelacnel_shenq(A)
qaxaq.tpel_shenqeris_cucak()
A.tur_hasce()
qaxaq.pntrel_yst_bnakaranneri(50)

qaxaq.grel_fayli_mej("qaxaq1")
qaxaq.poxel_poxoci_anuny("Sos Sargsyan","Միլիոն")
qaxaq.grel_fayli_mej("qaxaq2")
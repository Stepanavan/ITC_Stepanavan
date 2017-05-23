#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import objects


A=objects.ket(0.0,0.0)
B=objects.ket(0.0,0.0)
C=objects.ket(0.0,0.0)
D=objects.ket(0.0,0.0)
A.x= float(raw_input("Մուտքագրեք A կետի x կոորդինատը։ "))
A.y= float(raw_input("Մուտքագրեք A կետի y կոորդինատը։ "))
B.x= float(raw_input("Մուտքագրեք B կետի x կոորդինատը։ "))
B.y= float(raw_input("Մուտքագրեք B կետի y կոորդինատը։ "))
C.x= float(raw_input("Մուտքագրեք C կետի x կոորդինատը։ "))
C.y= float(raw_input("Մուտքագրեք C կետի y կոորդինատը։ "))
D.x= float(raw_input("Մուտքագրեք D կետի x կոորդինատը։ "))
D.y= float(raw_input("Մուտքագրեք D կետի y կոորդինատը։ "))

ABC=objects.erankyun(A,B,C)
ABD=objects.erankyun(A,B,D)
ACD=objects.erankyun(A,C,D)
BCD=objects.erankyun(B,C,D)
if -0.0000000001 <(ABC.makeres-ABD.makeres-ACD.makeres-BCD.makeres)<0.0000000001:
	print "D կետը պատկանում է ABC եռանկյանը"
else:
	print "D կետը չի պատկանում ABC եռանկյանը"

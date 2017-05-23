#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
from objects import *


A=ket(0.0,0.0)
B=ket(0.0,0.0)
C=ket(0.0,0.0)

A.x= float(raw_input("Մուտքագրեք A կետի x կոորդինատը։ "))
A.y= float(raw_input("Մուտքագրեք A կետի y կոորդինատը։ "))
B.x= float(raw_input("Մուտքագրեք B կետի x կոորդինատը։ "))
B.y= float(raw_input("Մուտքագրեք B կետի y կոորդինատը։ "))
C.x= float(raw_input("Մուտքագրեք C կետի x կոորդինատը։ "))
C.y= float(raw_input("Մուտքագրեք C կետի y կոորդինատը։ "))

ABC=erankyun(A,B,C)


r=(2*ABC.makeres)/ABC.paragits
print 'Ներգծած շրջանագծի շառավղի երկարությունն է ',r

R=erkarutyun(A,B)*erkarutyun(A,C)*erkarutyun(C,B)/(4*ABC.makeres)
print 'Արտագծած շրջանագծի շառավղի երկարությունն է ',R
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

print 'Ներգծած շրջանագծի շառավղի երկարությունն է ',ABC.r
print "ներգծած շրջանագծի կենտրոնի կոորդինատներն են: x= ", ABC.Or.x, ",", "y=",ABC.Or.y
print 'Արտագծած շրջանագծի շառավղի երկարությունն է ',ABC.R
print "Արտագծած շրջանագծի կենտրոնի կոորդինատներն են: x= ", ABC.OR.x, ",", "y=",ABC.OR.y

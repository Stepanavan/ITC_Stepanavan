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

ket_AB=ket((A.x+B.x)/2,(A.y+B.y)/2)
ket_AC=ket((A.x+C.x)/2,(A.y+C.y)/2)
uxix_AB=uxix(A,B)
uxix_AC=uxix(A,C)
uxix_BC=uxix(B,C)

uxxahayac_AB=uxix(A,ket_AB)
uxxahayac_AB.k=(1/uxix_AB.k)
uxxahayac_AB.b=ket_AB.y-uxxahayac_AB.k*ket_AB.x


uxxahayac_AC=uxix(A,ket_AC)
uxxahayac_AC.k=(1/uxix_AC.k)
uxxahayac_AC.b=ket_AC.y-uxxahayac_AC.k*ket_AC.x

x=(-1)*(uxxahayac_AB.b-uxxahayac_AC.b)/(uxxahayac_AB.k-uxxahayac_AC.k)
y=uxxahayac_AB.k*x+uxxahayac_AB.b
OR=ket(x,y)

print "Արտագծած շրջանագծի կենտրոնի կոորդինատներն են: x= ", OR.x, ",", "y=",OR.y


a1=math.atan(uxix_AB.k)
print a1
a2=math.atan(uxix_AC.k)
print a2
a=(a1+a2)/2

k=math.tan(a)

kisord_a=uxix(A,B)
kisord_a.k=k
kisord_a.b=A.y-kisord_a.k*A.x

a1=math.atan(uxix_AB.k)
a2=math.atan(uxix_BC.k)
a=(a1+a2)/2

k=math.tan(a)

kisord_b=uxix(C,B)
kisord_b.k=k
kisord_b.b=B.y-kisord_b.k*B.x

x=(-1)*(kisord_a.b-kisord_b.b)/(kisord_a.k-kisord_b.k)
y=kisord_a.k*x+kisord_a.b

Or=ket(x,y)


print "ներգծած շրջանագծի կենտրոնի կոորդինատներն են: x= ", Or.x, ",", "y=",Or.y

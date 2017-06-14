#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import objects

A=objects.ket(0.0,0.0)
B=objects.ket(10.0,0.0)
C=objects.ket(0.0,10.0)
D=objects.ket(5.0,5.0)
ABC=objects.erankyun(A,B,C)
ABD=objects.erankyun(A,B,D)
ACD=objects.erankyun(A,C,D)
BCD=objects.erankyun(B,C,D)
print ABC.makeres-ABD.makeres-ACD.makeres-BCD.makeres
if -0.0000000001 <(ABC.makeres-ABD.makeres-ACD.makeres-BCD.makeres)<0.0000000001:
	print "D կետը պատկանում է ABC եռանկյանը"
else:
	print "D կետը չի պատկանում ABC եռանկյանը"

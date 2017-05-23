#!/usr/bin/python
# -*- coding: utf-8 -*-
import xax_main
import os

xax_main.sarqel()
xax_main.och_to_file_xo()

while True:
 if (xax_main.qayl()%2==1):
  if xax_main.qayl()==1:
   print xax_main.qayl()
   xaxacox1=raw_input("Nermutseq Dzer Anun@: ")
   print xaxacox1, " duq xaxum eq x-ov"
  xax_main.refresh()
  mutq = int(raw_input("Nermutseq Dashti Hamar@: "))
  xax_main.och[mutq-1]= 'X'
  xax_main.och_to_file_xo()
  if xax_main.stugum('X'):
   print "haxtec X-y"
   break
  if xax_main.stugum('O'):
   print "haxtec O-y"
   break
  if xax_main.qayl()==10:
   print "voch voqi"
   break
  xax_main.refresh()
  if xax_main.stugum('X'):
   print "haxtec X-y"
   break
  if xax_main.stugum('O'):
   print "haxtec O-y"
   break
  if xax_main.qayl()==10:
   print "voch voqi"
   break
 else:
  os.system('clear')
  xax_main.refresh()
  if xax_main.stugum('X'):
   print "haxtec X-y"
   break
  if xax_main.stugum('O'):
   print "haxtec O-y"
   break
  if xax_main.qayl()==10:
   print "voch voqi"
   break
#!/usr/bin/python
# -*- coding: utf-8 -*-
import xax_main
import os

xax_main.sarqel2()
xax_main.och_to_file_xo()

while True:
 if (xax_main.qayl()%2==0):
  if xax_main.qayl()==2:
   print xax_main.qayl()
   xaxacox2=raw_input("Nermutseq Dzer Anun@: ")
   print xaxacox2, " duq xaxum eq O-ov"
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
  mutq = int(raw_input("Nermutseq Dashti Hamar@: "))
  xax_main.och[mutq-1]= 'O'
  xax_main.och_to_file_xo()
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
 
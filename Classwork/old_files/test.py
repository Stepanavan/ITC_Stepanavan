#!/usr/bin/python
import datetime
def aaa():
 "Barev dzez"
 try:
  datetime.date(2017, 4, 20)
 except ValueError:
  print "katarel eq sxal mutq"
 else:
  print datetime.date(2017, 4, 20)
  return 

aaa()
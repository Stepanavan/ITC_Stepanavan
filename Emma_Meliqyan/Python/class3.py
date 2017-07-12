#!/usr/bin/python
# -*- coding: utf-8 -*-
class First: 
     color = "red" 
     size =50
     def tpel(self): 
          print (self.color + "!")
          print (str(self.size) + "!")
     def poxel(self): 
          self.color = raw_input("nermutsel nor guyn: ")
class Second(First): 
     size = 60 
     def tpel(self): 
          print (self.color + "!")

obj1 = First() 
obj2 = First()
obj1.tpel()
obj2.tpel()
obj1.poxel() 
obj1.tpel() 
obj3=Second() 
obj3.tpel() 
obj3.poxel() 
obj3.tpel() 
print obj3.size
obj3.size=55 
print obj3.size
   

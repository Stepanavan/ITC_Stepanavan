#!/usr/bin/python

class First:
     color = "red"
     size =50
     def __init__(self):
          print ("Obyekty sarqe")
     def out(self):
          print (self.color + "!")
          print (str(self.size) + "!")
     def __del__(self):
          print ("Obyekt@ jnjeci")

asdasdasdasdasd = First()
obj2 = First() 

obj2.color="blue"

asdasdasdasdasd.out()
obj2.out()

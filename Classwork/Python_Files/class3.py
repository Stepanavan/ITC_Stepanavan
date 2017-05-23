#!/usr/bin/python
# -*- coding: utf-8 -*-
class First: #Класс
     color = "red" #Переменная класса
     size =50 #Переменная класса
     def tpel(self): #Метод класса
          print (self.color + "!")
          print (str(self.size) + "!")
          return
     def poxel(self): #Метод класса
          self.color = raw_input("nermutsel nor guyn: ")
          return
class Second(First): #Наследованный класс Second от класса First
     size = 60 #Перегруженный оператор класса
     def tpel(self): #Перегруженная функция класса
          print (self.color + "!")
          return

obj1 = First() #Экземпляр класса
obj2 = First() #Экземпляр класса
obj1.tpel() #Вызов метода
obj2.tpel() #Вызов метода
obj1.poxel() #Вызов метода
obj1.tpel() #Вызов метода
obj3=Second() #Экземпляр класса
obj3.tpel() #Вызов метода
obj3.poxel() #Вызов метода
obj3.tpel() #Вызов метода
print obj3.size
obj3.size=55 #Вызов оператора
print obj3.size
   

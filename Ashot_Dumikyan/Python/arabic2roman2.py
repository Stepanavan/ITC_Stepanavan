#!/usr/bin/python
# -*- coding: utf-8 -*-


num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def num2roman(num):

    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    return roman

#num = input("ներմուծել արաբական թիվը  ")
#print num2roman(num)

class arabic():
    def __init__(self, num):
        self.num = num
        print self.num
    def tpel(self):
        print self.num
        
class roman(arabic):
    def __init__(self, arabic):
        self.num = num2roman(arabic.num)
        print self.num

a1 = arabic(456)
r1 = roman(a1)
#r1.tpel()
a1.tpel()
        



#!/usr/bin/python
# -*- coding: utf-8 -*-

def arabic_to_roman(number):
    conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
            [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
            [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
            [   1, 'I']]
    result = ''
    for denom, roman_digit in conv:
        result += roman_digit*(number/denom)
        number %= denom
    return result

#for i in 1,4,9,16,25,49,81,1963,2015:
    #print i, arabic_to_roman(i)



number = input("ներմուծել արաբական թիվը  ")
print arabic_to_roman(number)
#!/usr/bin/python
# -*- coding: utf-8 -*-
x = float(raw_input('first number: '))
y = float(raw_input('second number: '))
operation = raw_input("operation: ")

result = None

if operation == '+':
    result = x+y
elif operation == '-':
    result = x-y
elif operation == '*':
    result = x*y
elif operation == '/':
    result = x/y
elif operation == '**':
    result = x**y
elif operation == '//':
    result = x//y
elif operation == '%':
    result = x%y   
else:
    print('unsupported operation')

if result is not None:
    print('Result:', result)

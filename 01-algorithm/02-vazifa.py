# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 23:22:04 2021

@author: WINDOWS 10
"""

# Eng kattasini qaytaruvchi algoritm .
print("3 ta son kiriting\n")
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a>b and a>c:
    print(a)
elif a<b and b>c:
    print(b)
else:
    print(c)
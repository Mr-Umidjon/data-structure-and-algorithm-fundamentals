# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 23:28:03 2021

@author: WINDOWS 10
"""

# N faktorialni hisoblovchi algoritm.
n = int(input("N ning qiymatini kiriting "))
faktorial = 1
i = 1

while i<=n:
    faktorial = faktorial * i
    i += 1
print(f"{n} faktorial {faktorial} ga teng")
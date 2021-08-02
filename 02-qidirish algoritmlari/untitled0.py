# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 09:25:52 2021

@author: WINDOWS 10
"""

#01 Uchta son berilgan. Shu sonlardan kichigini aniqlovchi programma tuzilsin.

def min_top(a, b, c):
    if a<=b and a<=c:
        return a
    elif b<=c and b<=a:
        return b
    else:
        return c
    
#02 Berilgan yilda necha kun borligini hisoblovchi dastur. 100 karrali yillar ichida faqat 400 ga
# karrali bo'lganlari kabisa yili hisoblanadi.
def yil_kun(yil):
    if yil>0:
        if yil%4==0 and yil%400==0:
            print(366)
        else:
            print(365)
            
#03
def funk(a, b):
    if a>b:
        c = b
        b = (a+c)/2
        a = 2*a*c
        return f"{a} {b}"
    elif b>a:
        c = a
        a = (c+b)/2
        b = 2*b*c
        return f"{a} {b}"   
    else:
        return f"{a} {b}"
    
#04
def sana(kun, oy):
    if kun<=31 and oy<=12:
        
    
    
    
    
    
    
    
    
    
    
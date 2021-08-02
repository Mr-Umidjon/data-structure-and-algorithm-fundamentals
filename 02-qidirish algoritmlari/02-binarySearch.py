# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:10:22 2021

@author: WINDOWS 10
"""

def binary_search(list, item):
    low=0;
    high=len(list)-1
    while low<=high:
        mid = (low+high)//2
        guess = list[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None     
        
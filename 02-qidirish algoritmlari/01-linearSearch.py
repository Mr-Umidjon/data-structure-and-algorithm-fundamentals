# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:07:50 2021

@author: WINDOWS 10
"""

def linear_search(list, item):
    for n in range(len(list)):
        if list[n]==item:
            return n
    return None
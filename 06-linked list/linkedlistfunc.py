# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 07:28:27 2021

@author: WINDOWS 10
"""

class Node:
    """Tugun (node) obyekti"""
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    """Linked List obyekti"""
    def __init__(self):
        self.head = None
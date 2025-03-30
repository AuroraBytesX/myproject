# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:07:29 2024

@author: tapas
"""

def largest(a,b):
    
        if a<b:
            print("the largest number is ",b)
        else:
            print("the laregest number is ",a)
    

try:
    x=int(input("enter first number :"))
    y=int(input("enter second number :"))
    largest(x,y)
except ValueError:
    print("please enter int")

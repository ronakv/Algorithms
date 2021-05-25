# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:04:12 2021

@author: ronak
"""
import math


def addZeros(num, N):
    s_num = str(num)
    i = 1;
    while (i <= N):
        s_num += "0"
        i = i + 1
        
    return int(s_num)

def karatsubaMultiply(x, y):
    
    n_x = len(str(x))
    n_y = len(str(y))
    
    if(x < 10 and y < 10):
        return x * y
  
         
    else:
        n = max(n_x, n_y)
        if(n%2 !=0):
            n = n-1
        a = math.trunc(x//10**(math.ceil(n/2)))
        b = x % 10**(math.ceil(n/2))
        c = math.trunc(y//10**(math.ceil(n/2)))
        d = y % 10**(math.ceil(n/2))
        
        
        ac = karatsubaMultiply(a, c)
        ad = karatsubaMultiply(a, d)
        bd = karatsubaMultiply(b, d)
        bc = karatsubaMultiply(b, c)
       
        if(n_x == n_y):
            return addZeros(ac, n) + addZeros(ad + bc, math.floor(n/2)) + bd
        else:
            return addZeros(ac, n) + addZeros(ad + bc, math.ceil(n/2)) + bd
    
a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627
test = karatsubaMultiply(a, b)

print(test == a*b)
    
    


    

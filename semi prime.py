# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def prime(m):
    if m > 1:
        if m == 2 or m == 3:
            return True
        for i in range(2, m):
            if m % i == 0:
                return False
            else:
                return True
    else:
        return False
def primeproduct(m):
    for i in range(1,m):
        if m%i == 0 and prime(i) and prime(m//i):
            return True
            break
    return False
            
print(prime(2))
print(prime(6))   
print(primeproduct(188))
print(primeproduct(10))

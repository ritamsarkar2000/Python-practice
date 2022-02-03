# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 11:36:31 2020

@author: RITAM
"""


from string import punctuation as pun

# to omit the symbols tp exclude them
def notpun(n):
  if n in list(pun):
    return False
  else:
    return True
  
#to get the string by joining them from a list  
def jn(n):
  finalstring = ''.join(n)
  return finalstring

#to decode
def decode():
  n, m = input().split()
  n,m = int(n), int(m)
  mat = []
  for i in range(n):
    l = input().split()
    mat.append(l)
    
  col = 0
  dec = []
  while col < m:
    for i in range(n):
      if notpun(mat[i][col]):
        dec.append(mat[i][col])
    col += 1
    
  fs = jn(dec)
  print(fs, end = '')
  
#calling the function
decode()
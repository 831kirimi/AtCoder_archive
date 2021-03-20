#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
N = int(input())

number = 0
maxn = int( (math.log10(N)+1)/2 ) 
#for i in range(1,maxn+1):
#  for j in range(10**(2*i-1),10**(2*i)):
#    if j > N:
#      break
#    s = str(j)
#    shimo = ""
#    kami = ""
#    for k in range(i):
#      shimo = shimo + s[-1-k]
#      kami = kami +  s[-1-k-i]
#    if shimo == kami:
#      number += 1
#print(number)

for i in range(1,maxn+1):
  for j in range(10**(i-1),10**i):
    s = str(j)
    if int(s+s)>N:
      break
    else:
      number +=1
print(number)

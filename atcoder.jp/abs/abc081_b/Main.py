#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
number = 0
a = False
for i in range(100000000):
  for j in range(N):
    if A[j]%2==0:
      A[j] = int(A[j]*0.5)
    else:
      a = True
      break
  if a == True:
    break
  number += 1
print(number)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import math
import copy

def P(n, r):
  return math.factorial(n) // math.factorial(n - r)

def main():
  N = list(input()) 
  N.sort(reverse=True)
  n = -(-len(N)//2)
  ans = []
  for i in range(n):
    L = list(itertools.permutations(N, r=i+1))
    for j in range(P(len(N),i+1)):
      l2 = copy.copy(N)
      l1 = L[j]
      for k in range(len(l1)):
        l2.remove(l1[k])
      ans.append(int("".join(l1))*int("".join(l2)))
        
  print(max(ans))


if(__name__ == '__main__'):
  main()

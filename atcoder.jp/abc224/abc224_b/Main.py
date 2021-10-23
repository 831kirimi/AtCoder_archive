#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  HW = list(map(int, input().split()))
  H = HW[0]
  W = HW[1]
  A = []
  for i in range(H):
    A.append(list(map(int, input().split())))
  end = False
  for i1 in range(H):
    for i2 in range(i1+1,H):
      for j1 in range(W):
        for j2 in range(j1+1,W):
          if A[i1][j1] + A[i2][j2] > A[i2][j1]+A[i1][j2]:
            print('No')
            end = True
            break
        if end:
          break
      if end:
        break
    if end:
      break
  if end == False:
    print('Yes')

if(__name__ == '__main__'):
  main()

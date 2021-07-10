#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  NX = list(map(int, input().split()))
  N = NX[0]
  X = NX[1]
  A = list(map(int, input().split()))
  sum = 0
  for i in range(N):
    if i % 2 == 0:
      sum += A[i]
    else:
      sum += A[i] - 1
  if sum > X:
    print('No')
  else:
    print('Yes')



if(__name__ == '__main__'):
  main()

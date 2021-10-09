#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  NP = list(map(int, input().split()))
  N = NP[0]
  P = NP[1]
  a = list(map(int, input().split()))
  count = 0
  for i in range(N):
    if a[i] < P:
      count += 1
  print(count)

if(__name__ == '__main__'):
  main()

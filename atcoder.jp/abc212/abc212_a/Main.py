#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():

  n = list(map(int, input().split()))
  A = n[0]
  B = n[1]
  if 0 < A and B == 0:
    ans = 'Gold'
  elif A == 0 and 0 < B:
    ans = 'Silver'
  else:
    ans = 'Alloy'
  print(ans)

if(__name__ == '__main__'):
  main()

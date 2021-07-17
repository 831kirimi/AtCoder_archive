#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  l = list(map(int, input().split()))
  N = l[0]
  A = l[1]
  X = l[2]
  Y = l[3]
  if N > A:
    ans = X * A + Y * (N - A)
  else:
    ans = X * N
  print(ans)
if(__name__ == '__main__'):
  main()

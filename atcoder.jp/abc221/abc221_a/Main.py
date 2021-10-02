#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  AB = list(map(int, input().split()))
  A = AB[0]
  B = AB[1]
  d = A - B
  ans = 1
  for i in range(d):
    ans *= 32
  print(ans)

if(__name__ == '__main__'):
  main()

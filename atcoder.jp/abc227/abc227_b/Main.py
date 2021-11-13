#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  n = int(input()) 
  s = list(map(int, input().split()))
  ans = 0
  for i in range(len(s)):
    a = 1
    while s[i]-3*a>=4*a+3:
      if (s[i]-3*a)%(4*a+3) == 0:
        break
      a += 1
    else:
      ans += 1
  print(ans)



if(__name__ == '__main__'):
  main()

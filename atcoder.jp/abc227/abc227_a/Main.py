#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  
  l = list(map(int, input().split()))
  n = l[0]
  k = l[1]
  a = l[2]
  if (a+k-1)%n != 0:
    print((a+k-1)%n)
  else:
    print(n)


if(__name__ == '__main__'):
  main()

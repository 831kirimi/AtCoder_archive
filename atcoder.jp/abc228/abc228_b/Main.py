#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  n,x = map(int, input().split())
  a = list(map(int, input().split()))

  i = x
  known = {i:0}
  while(a[i-1] not in known):
    known[a[i-1]] = 0
    i = a[i-1]
  print(len(known))


if(__name__ == '__main__'):
  main()

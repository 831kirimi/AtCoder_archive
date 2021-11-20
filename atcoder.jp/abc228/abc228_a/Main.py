#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  s,t,x = map(int, input().split())
  if s <= t:
    if s <= x and x < t:
      print('Yes')
    else:
      print('No')
  else:
    if (0 <= x and x < t) or (s <= x and x < 24):
      print('Yes')
    else:
      print('No')


if(__name__ == '__main__'):
  main()

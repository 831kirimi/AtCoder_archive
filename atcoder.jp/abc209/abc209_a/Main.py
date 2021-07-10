#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  AB = list(map(int, input().split()))
  if AB[1] - AB[0] >=0:
    print(AB[1] - AB[0] + 1)
  else:
    print('0')

if(__name__ == '__main__'):
  main()

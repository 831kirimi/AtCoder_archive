#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  AB = list(map(int, input().split()))
  A = AB[0]
  B = AB[1]
  C = (A-B)/3 + B
  print(C)
if(__name__ == '__main__'):
  main()

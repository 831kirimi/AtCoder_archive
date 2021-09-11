#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  P = list(map(int, input().split()))
  Alp = 'abcdefghijklmnopqrstuvwxyz'
  for i in range(len(P)):
    print(Alp[P[i]-1],end="")

if(__name__ == '__main__'):
  main()

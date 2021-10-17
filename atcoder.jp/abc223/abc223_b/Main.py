#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  N = str(input()) 
  S = []
  for i in range(len(N)):
    S.append(N[i:]+N[:i])
  S.sort()

  print(S[0])
  print(S[-1])

if(__name__ == '__main__'):
  main()

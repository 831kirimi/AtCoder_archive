#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  S = str(input()) 
  n = 0
  if S[0] == S[1]:
    n = 1
  elif S[0] == S[2]:
    n = 1
  elif S[1] == S[2]:
    n = 1
  if S[0] == S[1] == S[2]:
    n  = 2
  if n == 0:
    print(6)
  elif n == 1:
    print(3)
  elif n == 2:
    print(1)


if(__name__ == '__main__'):
  main()

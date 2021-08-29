#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  A = list(map(int, input().split(".")))
  X = A[0]
  Y = A[1]
  if 0 <= Y and Y <= 2:
    print(X,'-',sep='')
  elif Y <= 6:
    print(X)
  else:
    print(X,'+',sep='')

if(__name__ == '__main__'):
  main()

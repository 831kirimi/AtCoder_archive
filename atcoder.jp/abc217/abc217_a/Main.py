#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  A = list(map(str, input().split()))
  A_sort = sorted(A)
  if A == A_sort:
    print('Yes')
  else:
    print('No')

if(__name__ == '__main__'):
  main()

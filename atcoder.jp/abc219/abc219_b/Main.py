#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  S = []
  S.append(str(input()))
  S.append(str(input()))
  S.append(str(input()))
  T = list(input())
  for i in range(len(T)):
    print(S[int(T[i])-1],end='')

if(__name__ == '__main__'):
  main()

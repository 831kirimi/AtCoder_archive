#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  S = []
  S.append(str(input()))
  S.append(str(input()))
  S.append(str(input()))

  T = ['ABC' , 'ARC' , 'AGC' , 'AHC']

  for i in range(3):
    T.remove(S[i])

  print(T[0])


if(__name__ == '__main__'):
  main()

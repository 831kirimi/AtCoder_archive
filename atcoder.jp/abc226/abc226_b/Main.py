#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  n = int(input()) 
  l = []
  for i in range(n):
    l.append(input())
  d = {}
  for i in range(n):
    d[l[i]] = 1
  print(len(d))


if(__name__ == '__main__'):
  main()

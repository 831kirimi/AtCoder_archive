#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  N = int(input()) 
  S = str(input()) 
  if S[N-1] == 'o':
    print('Yes')
  else:
    print('No')

if(__name__ == '__main__'):
  main()

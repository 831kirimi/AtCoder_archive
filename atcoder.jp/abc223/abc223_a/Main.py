#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  N = int(input()) 
  if N % 100 == 0 and N != 0:
    print('Yes')
  else:
    print('No')

if(__name__ == '__main__'):
  main()

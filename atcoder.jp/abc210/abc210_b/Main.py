#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  N = int(input()) 
  S = str(input()) 
  if S.find('1') %2 == 0:
    print('Takahashi')
  else:
    print('Aoki')


if(__name__ == '__main__'):
  main()

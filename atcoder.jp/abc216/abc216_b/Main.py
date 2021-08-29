#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  N = int(input()) 
  ST = []
  for i in range(N):
    ST.append(str(input()))
  ans = 0
  for i in range(N):
    for j in range(N-i-1):
      if ST[i] == ST[i+j+1]:
        ans = True
        break
  if ans:
    print('Yes')
  else:
    print('No')



if(__name__ == '__main__'):
  main()

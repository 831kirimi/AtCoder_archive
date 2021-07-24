#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  S1 = str(input()) 
  S2 = str(input()) 
  S3 = str(input()) 
  S4 = str(input()) 
  S = []
  S.append(S1)
  S.append(S2)
  S.append(S3)
  S.append(S4)

  H = 0
  B2 = 0
  B3 = 0
  HR = 0

  for i in range(4):
    if S[i] == 'H':
      H = 1
    elif S[i] == '2B':
      B2 = 1
    elif S[i] == '3B':
      B3 = 1
    elif S[i] == 'HR':
      HR = 1
  if H == 1 and B2 == 1 and B3 == 1 and HR == 1:
    print('Yes')
  else:
    print('No')

if(__name__ == '__main__'):
  main()

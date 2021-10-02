#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  S = str(input()) 
  T = str(input()) 
  difS = []
  difT = []
  n = []
  for i in range(len(S)):
    if S[i] != T[i]:
      difS.append(S[i])
      difT.append(T[i])
      n.append(i)
  if len(difS) == 0 or (len(difS) == 2 and difS[0] == difT[1] and difS[1] == difT[0] and n[1] - n[0] == 1):
    print('Yes')
  else:
    print('No')



if(__name__ == '__main__'):
  main()

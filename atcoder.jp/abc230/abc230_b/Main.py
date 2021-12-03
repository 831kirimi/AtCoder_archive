#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  s = input()
  S = "oxxoxxoxxoxxoxx"
  n = len(s)
  s1 = S[0:n]
  s2 = S[1:n+1]
  s3 = S[2:n+2]
  
  if s == s1 or s == s2 or s == s3:
    print('Yes')
  else:
    print('No')





if(__name__ == '__main__'):
  main()

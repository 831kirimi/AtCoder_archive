#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  X = str(input()) 
  if X[0] == X[1] and X[0] == X[2] and X[0] == X[3]:
    ans = 'Weak'
       
  else:
    ans = 'Strong'
  count = 0
  for i in range(3):
    if (int(X[i]) < 9 and int(X[i]) + 1 == int(X[i+1])) or (int(X[i]) == 9 and int(X[i+1]) == 0):
      count += 1
    else:
      break
  if count == 3:
    ans = 'Weak'
  print(ans)


if(__name__ == '__main__'):
  main()

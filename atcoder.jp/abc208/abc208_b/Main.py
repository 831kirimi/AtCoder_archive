#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():

  P = int(input()) 
  sum = 0
  for i in range(10):
    coin = 1
    for j in range(10-i):
      coin = coin * (j+1)
    if P >= coin:
      sum = sum + int(P/coin)
      P = P - coin*int(P/coin)

  print(sum)

if(__name__ == '__main__'):
  main()

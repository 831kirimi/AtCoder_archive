#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  NK = list(map(int, input().split()))
  N = NK[0]
  K = NK[1]
  a = list(map(int, input().split()))

  initial = K //N 
  K -= N*initial
  if K == 0:
    for i in range(N):
      print(initial)
  elif K <= N:
    sort_a = sorted(a)
    max_a = int(sort_a[K-1])
    for i in range(N):
      if a[i] <= max_a:
        print(initial+1)
      else:
        print(initial)
  else:
    print('error!')

if(__name__ == '__main__'):
  main()

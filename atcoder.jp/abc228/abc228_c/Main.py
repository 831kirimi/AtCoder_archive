#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  n,k = map(int, input().split())
  p = [list(map(int, input().split())) for _ in range(n)]
  p_sum = [sum(p[i]) for i in range(n)]
  p_sum_sort = sorted(p_sum, reverse=True) 

  border = p_sum_sort[k-1]
    

  for i in range(n):
    if p_sum[i]+300 >= border:
      print('Yes')
    else:
      print('No')


if(__name__ == '__main__'):
  main()

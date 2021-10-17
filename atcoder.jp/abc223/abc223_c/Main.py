#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
  N = int(input()) 
  AB = []
  for i in range(N):
    AB.append(list(map(int, input().split())))
  #i番目のひもかかる時間
  T = [0]*N
  #全部の長さ
  total_l = 0
  #全部燃えるのにかかる時間
  total_t = 0
  for i in range(N):
    total_l += AB[i][0]
    T[i] = AB[i][0]/AB[i][1]
    total_t += T[i]

  count0t = 0
  count0l = 0
  for i in range(N):
    if count0t+T[i] >= (total_t/2):
      ans = count0l + AB[i][1]*(total_t/2-count0t)
      print(ans)
      break
    count0l += AB[i][0]
    count0t += T[i]

    


if(__name__ == '__main__'):
  main()

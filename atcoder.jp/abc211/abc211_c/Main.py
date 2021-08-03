#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
  S = str(input()) 
  N = len(S)
  T = 'chokudai'
  M = len(T)
  mod = 10**9+7
  dp=[[0]*(M+1) for _ in range(N+1)]
  for i in range(N+1):
    for j in range(M+1):
      if j == 0:
        dp[i][j] = 1
      elif i == 0:
        dp[i][j] = 0
      elif S[i-1] == T[j-1]:
        dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % mod
      else:
        dp[i][j] = dp[i-1][j]  % mod
  print(dp[N][M])



if(__name__ == '__main__'):
  main()

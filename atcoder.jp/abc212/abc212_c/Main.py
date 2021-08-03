#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  NM = list(map(int, input().split()))
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  N = NM[0]
  M = NM[1]
  A.sort()
  B.sort()
  ans = min(abs(A[0]-B[0]),abs(A[0]-B[M-1]),abs(A[N-1]-B[0]),abs(A[N-1]-B[M-1]))

  i = 0
  j = 0
  while i < N and j < M:
    ans = min(ans,abs(A[i]-B[j]))
    if A[i] > B[j]:
      j += 1
    else:
      i += 1
  print(ans)

      
      


if(__name__ == '__main__'):
  main()

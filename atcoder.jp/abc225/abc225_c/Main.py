#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  NM = list(map(int, input().split()))
  N = NM[0]
  M = NM[1]
  B = []
  for i in range(N):
    B.append(list(map(int, input().split())))

  i0 = B[0][0] // 7
  j0 = B[0][0] % 7
  ans = True
  if j0 == 0 and M>1:
    ans = False
  elif j0 != 0 and j0+M-1 > 7:
    ans = False

  for i in range(N):
    for j in range(M):
      if B[i][j] != 7*(i0+i)+j0+j:
        ans = False
        break
  if ans == True:
    print('Yes')
  else:
    print('No')



if(__name__ == '__main__'):
  main()

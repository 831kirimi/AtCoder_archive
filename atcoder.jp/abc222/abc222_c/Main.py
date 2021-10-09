#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def jan(i,j):
  if i == j:
    return[0, 0]
  elif (i == 'G' and j == 'C') or (i == 'C' and j == 'P') or (i == 'P' and j == 'G'):
    return [1, 0]
  elif (j == 'G' and i == 'C') or (j == 'C' and i == 'P') or (j == 'P' and i == 'G'):
    return [0, 1]
  
def main():
  NM = list(map(int, input().split()))
  N = NM[0]
  M = NM[1]
#  A = [[] * M for i in range(2*N)]
  A = []
  for i in range(2*N):
    A.append(str(input()))

  point = []
  for i in range(2*N):
    point.append([i,0])

  for i in range(M):
    for j in range(N):
      a = point[2*j][0]
      b = point[2*j+1][0]
      point[2*j][1] += jan(A[a][i],A[b][i])[0]
      point[2*j+1][1] += jan(A[a][i],A[b][i])[1]
    point = sorted(point, reverse=False, key=lambda x: x[0])
    point = sorted(point, reverse=True, key=lambda x: x[1])
     
  for i in range(2*N):
    print(point[i][0]+1)


if(__name__ == '__main__'):
  main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  N = int(input()) 

  XY = []
  for i in range(N):
    XY.append(list(map(int, input().split())))
  ans = 0
  for i in range(N-2):
    for j in range(i+1,N-1):
      for k in range(j+1,N):
        if abs(XY[j][0] - XY[i][0]) > 10e5 and abs(XY[k][0] - XY[i][0]) > 10e5:
          A = XY[j]
          B = XY[i]
          C = XY[k]
        else:
          A = XY[i]
          B = XY[j]
          C = XY[k]


        AB0 = B[0] - A[0]
        AB1 = B[1] - A[1]
        AC0 = C[0] - A[0]
        AC1 = C[1] - A[1]

        if AC0 == 0:
          if AB0 != 0:
            ans += 1
        elif AC1 == 0:
          if AB1 != 0:
            ans += 1
        elif AB0 / AC0 != AB1 / AC1:
          ans += 1
  print(ans)
          




if(__name__ == '__main__'):
  main()

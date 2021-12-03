#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  n, a, b = map(int, input().split())
  p, q, r, s = map(int, input().split())
  
  x1 = max(1-a,1-b)
  x2 = min(n-a,n-b)
  y1 = max(1-a,b-n)
  y2 = min(n-a,b-1)

  for i in range(p, q+1):
    for j in range(r, s+1):
      if (i-a==j-b) and x1<=i-a<=x2:
        print('#', end='')
      elif (i-a==b-j) and y1<=i-a<=y2:
        print('#', end='')
      else:
        print('.', end='')
    print('\n')





    
  
if(__name__ == '__main__'):
  main()

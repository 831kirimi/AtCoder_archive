#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  N = int(input()) 
  ab = []
  for i in range(N-1):
    ab.append(list(map(int, input().split())))

  tree0 = True
  for i in range(1,N-1):
    if ab[i][0] != ab[0][0] and ab[i][1] != ab[0][0]:
      tree0 = False
      break
  tree1 = True
  for i in range(1,N-1):
    if ab[i][0] != ab[0][1] and ab[i][1] != ab[0][1]:
      tree1 = False
      break
  if tree0 or tree1:
    print('Yes')
  else:
    print('No')

if(__name__ == '__main__'):
  main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter
def main():
  NK = list(map(int, input().split()))
  c = list(map(int, input().split()))
  N = NK[0]
  K = NK[1]
  ans = []
  sub = Counter(c[0:K])
  ans.append(len(sub))
  for i in range(1,N-K+1):
    sub[c[i-1]] -= 1
    sub[c[i+K-1]] += 1
    if sub[c[i-1]] <= 0:
      del sub[c[i-1]]
    ans.append(len(sub))
#    print('---')
#    print(i,sub,len(sub))
#    print(i-1,i+K-1)
#    print(ans)
#  print(ans)
  print(max(ans))

if(__name__ == '__main__'):
  main()

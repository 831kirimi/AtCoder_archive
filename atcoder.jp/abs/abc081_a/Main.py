#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = list(input())

n = 0
for i in range(len(s)):
  s[i] = int(s[i])
  if s[i] == 1:
    n += 1
print(n)

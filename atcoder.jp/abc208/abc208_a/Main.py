#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: Jul, 04, 2021 21:00:57 by Ayame Suzuki
# $Author: $
# $Date: $
# $URL: $
__giturl__ = "$URL: $"

def main():
  i = list(map(int, input().split()))
  A = i[0]
  B = i[1]

  if A <= B <= 6*A:
    print('Yes')
  else:
    print('No')
if(__name__ == '__main__'):
  main()

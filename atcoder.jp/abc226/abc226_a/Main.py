#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN 
  n = input()
  ans = Decimal(n).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
  print(ans)

if(__name__ == '__main__'):
  main()

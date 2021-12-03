#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  n = int(input())
  if n < 42:
    n_zero = str(n).zfill(3)
    print("AGC"+n_zero)
  else:
    n += 1
    n_zero = str(n).zfill(3)
    print("AGC"+n_zero)

    

if(__name__ == '__main__'):
  main()

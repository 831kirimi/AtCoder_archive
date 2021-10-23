#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  S = str(input()) 
  if S[-2] + S[-1] == "er":
    print("er")
  elif S[-3] + S[-2] + S[-1] == "ist":
    print("ist")

if(__name__ == '__main__'):
  main()

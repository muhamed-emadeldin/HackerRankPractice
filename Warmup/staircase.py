#!/usr/bin/env

def staircase(n):
  s = ""
  k = "#"

  for i in range(1, n + 1):
    print((s * (n - i)) + k * (i))
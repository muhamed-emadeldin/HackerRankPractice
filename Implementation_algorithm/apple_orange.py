#!/usr/bin/python

def countApplesAndOranges(s, t, a, b, apples, oranges):
  #-->defense function
  assert(isinstance(s, int)), "S should integer"
  assert(isinstance(t, int)), "S should integer"
  assert(isinstance(a, int)), "S should integer"
  assert(isinstance(b, int)), "S should integer"
  assert(isinstance(apples, list)), "S should integer"
  assert(isinstance(oranges, list)), "S should integer"

  apple    = sum(s <= a + d <= t for d in apples)
  orange   = sum(s <= b + d <= t for d in oranges)

  print(apple, orange, sep="\n")


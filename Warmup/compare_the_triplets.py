#!/usr/bin/env python


def compareTriplets(a, b):
  #-->defense function
  assert(isinstance(a, list)), "AssertionError"
  assert(isinstance(b, list)), "AssertionError"

  if len(a) > len(b) or len(b) > len(a):
    return "length of two lists should be equal"

  #-->basic variables
  alice = 0
  bob   = 0
  n     = len(a)

  #--loop in range n
  for i in range(n):
    #-->defense function
    if not type(a[i]) is int or not type(b[i]) is int:
      return "element should be integers"

    if a[i] > b[i]:
      alice += 1
    elif a[i] < b[i]:
      bob   += 1

  return [alice] + [bob]

def compare_triplets_test():
  test_cases = [#--Edge cases
                ((None, [99, 16, 8]), "AssertionError"),
                (([17, 28, 30], [99, "16", 8]), "element should be integers"),
                (([17, 28, 30], [99, 16, 8]), [2, 1]),

               ]

  for (args, answer) in test_cases:
    try:
      result = compareTriplets(*args)

      if result == answer and answer != "AssertionError":
        print("Test Case is Passed !")
      else:
        print("Test case", args, "Failed")
    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(args))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(args))

compare_triplets_test()
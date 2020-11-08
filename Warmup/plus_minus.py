#!/usr/bin/env python
def plusMinus(arr):
  #-->defense function
  assert(isinstance(arr, list)), "AssertionError"

  #--basic variables
  zero_elm  = 0
  plus_em   = 0
  minus_elm = 0
  n         = len(arr)

  #-->get number of positive elm and minus elm 
  for elm in arr:
    if elm > 0:
      plus_em += 1
    elif elm < 0:
      minus_elm += 1
    else:
      zero_elm += 1
  
  #-->get ratio of each elm
  zero_elm  = '{0:.6f}'.format(zero_elm / n)
  minus_elm = '{0:.6f}'.format(minus_elm / n)
  plus_em   = '{0:.6f}'.format(plus_em / n)

  
  return zero_elm, minus_elm, plus_em


def plusMinus_test():
  test_cases  = [#-->Edge cases
                  (None, "AssertionError"),
                  ([-4, 3, -9, 0, 4, 1], ('0.166667', '0.333333', '0.500000')),
                ]

  for arg, answer in test_cases:
    try:
      result =  plusMinus(arg)
      if result == answer and answer != "AssertionError":
        print("Test Case Passed !")
      else:
        print("Test Case", arg, "Faild")

    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

plusMinus_test()

  
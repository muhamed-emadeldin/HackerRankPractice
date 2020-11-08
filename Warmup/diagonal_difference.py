#!/usr/bin/env python


def diagonalDifference(arr):
  #-->defense function
  assert(isinstance(arr, list)), "AssertionError"

  #-->basic variables
  start             = 0
  end               = -1
  n                 = len(arr) 
  primary_diagonal  = 0
  secondry_diagonal = 0

  #--> loop in range n
  for i in range(n):
    #-->defense function
    if type(arr[i]) is not list:
      return "object should be a list"
    if type(arr[i][start]) is not int or type(arr[i][end]) is not int:
      return "elements should be integer"

    primary_diagonal  += arr[i][start]
    secondry_diagonal += arr[i][end]

    start             += 1
    end               -= 1

  
  result  = primary_diagonal - secondry_diagonal
  return abs(result)

def diagonalDifference_test():
  test_cases  = [#-->Edge cases
                  (None, "AssertionError"),
                  ([[11, 2, 4], [4, 5, 6], None], "object should be a list"),
                  ([[11, 2, 4], [4, 5, 6], [10, 8, "-12"]], "elements should be integer"),

                  ([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15),
                ]

  for arg, answer in test_cases:
    try:
      result =  diagonalDifference(arg)
      if result == answer and answer != "AssertionError":
        print("Test Case Passed !")
      else:
        print("Test Case", arg, "Faild")

    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

diagonalDifference_test()



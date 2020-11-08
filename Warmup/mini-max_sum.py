#!/usr/bin/python

def miniMaxSum(arr):
  #-->defense function
  assert(isinstance(arr, list)), "AssertionError"

  for num in arr:
    assert(isinstance(num, int)), "AssertionError"

  #-->Check if array is sorted or no
  checkArr  = check_sorted_arr(arr)

  #-->if array unsorted sorted with heapSort
  if not checkArr:
    arr = heapSort(arr)

  #-->get mini value of first four num and max for end four number
  mini_val  = sum(arr[:-1])
  max_val   = sum(arr[1:])

  return mini_val, max_val

#-->check sorted array function helper
def check_sorted_arr(arr):
  sorted_elm  = [arr[index] < arr[index + 1] for index in range(len(arr) - 1)]
  return all(sorted_elm)

#-->heap Sort function helper to sort array
def heapSort(arr):
  #-->basic variables
  n = len(arr)

  #-->bulding mini heap sort
  for i in range(n, -1, -1):
    heapfiy(arr, n , i)

  #-->extract one by one
  for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapfiy(arr, i, 0)

  return arr

#-->implemention heapfiy
def heapfiy(arr, n, i):
  parent  = i
  lChild  = 2 * i + 1
  rChild  = 2 * i + 2

  #-->compare between left child and parent
  if lChild < n and arr[i] < arr[lChild]:
    parent  = lChild

  #-->compare between right child and parent
  if rChild < n and arr[parent] < arr[rChild]:
    parent  = rChild

  #-->if parent not equal i
  if parent != i:
    arr[i], arr[parent] = arr[parent], arr[i]
    heapfiy(arr, n, parent)


def test_miniMaxSum():
  test_cases  = [#-->Edge cases
                  (None, "AssertionError"),
                  ([1, 2, 3, 4, "5"], "AssertionError"),
                
                  #-->regular cases
                  ([1, 2, 3, 4, 5], (10, 14)),
                  ([1, 3, 5, 7, 9], (16, 24)),
                  ([9, 7, 5, 3, 1], (16, 24)),
                ]

  for arg, answer in test_cases:
    try:
      result  = miniMaxSum(arg)
      if result == answer and answer != "AssertionError":
        print("Test Case Pass!")
      else:
        print("Test Case", arg, "Faild")
    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

test_miniMaxSum()
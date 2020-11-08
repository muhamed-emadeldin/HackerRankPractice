#!/usr/bin/python

def birthdayCakeCandles(candles):
  #-->defense function
  assert(isinstance(candles, list)), "AssertionError"
  x = [i for i in candles if not isinstance(i, int)]
  if len(x) > 0:
    return -1

  #-->check if list sorted or no
  check_list  = all([candles[index] <= candles[index + 1] for index in range(len(candles) - 1)])

  #-->soretd list if list not sorted
  if not check_list:
    candles = quickSort(candles)

  return candles.count(candles[-1])

#-->implemention quick sort
def quickSort(arr):
  sortAll(arr, 0, len(arr) - 1)
  return arr

def sortAll(arr, start, end):
  if end <= start:
    return
    
  pivot = sort_a_little_bit(arr, start, end)
  left  = sortAll(arr, start, pivot - 1)
  right = sortAll(arr, pivot + 1, end)

def sort_a_little_bit(arr, start, end):
  i = end
  j = start
  pivot = arr[i]

  while i != j:
    item  = arr[j]

    if item <= pivot:
      j += 1
      continue
    
    #-->swap value of left index with value next item of povit
    arr[j]  = arr[i - 1]
    #-->shift povit index in next position
    arr[i - 1] = pivot
    #-->shift item position rather than pivot
    arr[i]  = item

    i -= 1

  return i
    




def test_birthdayCakeCandles():
  test_cases  = [#-->Edge cases
                  (None, "AssertionError"),
                  ([1, 2, 3, 4, "5"], -1),
                
                  #-->regular cases
                  ([1, 2, 3, 4, 5], 1),
                  ([9, 1, 3, 5, 7, 9], 2),
                  ([9, 7, 5, 3, 1, 9, 9, 9], 4),
                ]

  for arg, answer in test_cases:
    try:
      result  = birthdayCakeCandles(arg)
      if result == answer and answer != "AssertionError":
        print("Test Case Pass!")
      else:
        print("Test Case", arg, "Faild")
    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

test_birthdayCakeCandles()
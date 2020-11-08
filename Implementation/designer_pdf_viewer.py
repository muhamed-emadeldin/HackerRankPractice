#!/usr/bin/python

def designerPdfViewer(h, word):
  #-->defense function
  assert(isinstance(h, list)), "AssertionError"
  assert(isinstance(word, str)), "AssertionError"

  #-->basic variables
  n     = len(word)
  tall  = 0

  #-->get max tall of charater
  for chr in word:
    if tall == 0:
      tall  = h[ord(chr) - ord("a")]
    
    else:
      tall  = max(tall, h[ord(chr) - ord("a")])

  return n * tall


#-->implemention function test
def test_case():
  test_case = [#-->Edge case
                ((None, "sd"), "AssertionError"),

                (([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7], "zaba"), 28),

                (([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7], "abc"), 9)
              ]

  for arg, answer in test_case:
    try:
      result  = designerPdfViewer(*arg)
      if result == answer and answer != "AssertErro":
        print("Test case Pass")
      else:
        print("Test case", arg, "Faild")
    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

test_case()

#!/usr/bin/env python

def timeConversion(s):
  #-->defense function
  assert(isinstance(s, str)), "AssertionError"

  #-->check if time end with "PM" or "AM"
  if s.endswith("AM"):
    s = s.replace("AM", "")
    s = s.split(":")
    if s[0] == "12":
      s[0] = "00"

  
  elif s.endswith("PM"):
    s = s.replace("PM", "")
    s = s.split(":")
    if s[0] != "12":
      if s[0].startswith("0"):
        s[0] = str(int(s[0][1]) + 12)
      else:
        s[0] = str(int(s[0]) + 12)
  
  else:
    return "Time should be end with AM or PM"
  
  return ":".join(s)



def timeConversion_test():
  test_cases = [#-->Edge cases
                (None, "AssertionError"),
                ("07:05:45", "Time should be end with AM or PM"),


                ("01:59:45AM", "01:59:45"),
                ("01:59:45PM", "13:59:45"),
                ("07:05:45PM", "19:05:45"),
                ("12:05:45AM", "00:05:45"),
                ("12:05:45PM", "12:05:45"),
               ]

  for arg, answer in test_cases:
    try:
      
      result  =  timeConversion(arg)

      if result == answer and answer != "AssertionError":
        print("Test Case Passed !")
      else:
        print("Test Case", arg, "Faild")

    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

timeConversion_test()
# print(timeConversion("07:05:45PM"))
#!/usr/bin/python


def viralAdvertising(n):
  #-->defense function
  assert(isinstance(n, int)), "N should Integer"

  #-->basic condation
  if n == 1:
    return 2

  #-->basic variables
  dic         = {"day" + str(key):0 for key in range(1, n+1)}
  dic["day1"] = 5
  cumulitve   = 2

  for i in range(2, n+1):
    dic["day" + str(i)] = (dic["day" + str(i - 1)] // 2) * 3
    cumulitve           += dic["day" + str(i)] // 2
  
  return cumulitve

print(viralAdvertising(1000))

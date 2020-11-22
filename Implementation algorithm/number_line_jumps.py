
def kangaroo(x1, v1, x2, v2):
  #-->defense function
  assert(isinstance(x1, int)), "x1 should be int"
  assert(isinstance(x2, int)), "x1 should be int"
  assert(isinstance(v1, int)), "x1 should be int"
  assert(isinstance(v2, int)), "x1 should be int"

  #-->basic variables
  k1 = x1 + v1
  k2 = x2 + v2

  #-->basic condation
  if x1 < x2 and v1 <= v2:
    return "NO"

  while True:
    k1 += v1
    k2 += v2
    
    if k1 == k2:
      return "YES"

    if k1 > k2:
      break
  
  return "NO"

# print(kangaroo(0,3, 4,2))
# print(kangaroo(3,42, 2,94))
# print(kangaroo(4,14, 2,98))
# print(kangaroo(7,45, 2,56))
print(kangaroo(2564,5393, 5121,2836))



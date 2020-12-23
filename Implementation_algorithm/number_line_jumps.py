
def kangaroo(x1, v1, x2, v2):
  #-->defense function
  assert(isinstance(x1, int)), "x1 should be int"
  assert(isinstance(x2, int)), "x1 should be int"
  assert(isinstance(v1, int)), "x1 should be int"
  assert(isinstance(v2, int)), "x1 should be int"

  #-->basic variables
  k1      = x1 + v1
  k2      = x2 + v2
  bigger  = which_bigger(k1, k2)

  #-->basic condation
  if x1 < x2 and v1 <= v2:
    return "NO"
  elif x1 > x2 and v1 >= v2:
    return "NO"

  while k1 != k2:
    if abs(k1 - k2) > bigger:
      return "NO", k1, k2
    
    k1 += v1
    k2 += v2

  return "YES", k1, k2

def which_bigger(n1, n2):
  if n1 > n2:
    return n1
  return n2

# print(kangaroo(0,3, 4,2))
# print(kangaroo(3,42, 2,94))
# print(kangaroo(4,14, 2,98))
# print(kangaroo(7,45, 2,56))
# print(kangaroo(2564,5393, 5121,2836))
print(kangaroo(0,2, 5,3))
print(kangaroo(2,1, 1,2))
print(kangaroo(43, 2, 70, 2))







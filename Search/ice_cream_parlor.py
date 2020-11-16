
'''
Here we loop in array until we get a difference between item and target and return indicies for each item
'''
def icecreamParlor(m, arr):
  #-->defense function
  assert(isinstance(m, int)), "Target should be integer"
  assert(isinstance(arr, list)), "arr should be list"
  
  #-->basic variables
  diff = {}

  for i in range(len(arr)):
    if m - arr[i] in diff:
      return diff[m-arr[i]], i + 1
    else:
      diff[arr[i]] = i + 1
  
    

print(icecreamParlor(20, [7, 8, 9, 10, 12]))
print(icecreamParlor(4, [1, 4, 5, 3, 2]))
print(icecreamParlor(8, [1, 3, 4, 4, 6, 8]))
print(icecreamParlor(4, [2, 2, 3, 4]))
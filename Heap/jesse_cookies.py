#!/usr/bin/env python

#create Class MiniHeap
class MiniHeap:
  #-->initial defention
  def __init__(self, capacity):
    self.cbt = [None for _ in range(2*capacity)]
    self.next_index = 0

  #-->insert defention
  def insert(self, data):
    # print("next index is:", self.next_index)
    self.cbt[self.next_index] = data
    self.up_heapfiy()
    self.next_index += 1

    #--> increase capacity of cbt
    if self.next_index >= self.size():
      temp = self.cbt
      self.cbt = [None for _ in range(2*len(self.cbt))]
      for i in range(len(temp)):
        self.cbt[i] = temp[i]

    

  #-->up_heapfiy defention helper the insert to make a root with miniumum value
  def up_heapfiy(self):
    child_index = self.next_index
    while child_index >= 1:
      parent_index  = child_index - 1
      parent_elm    = self.cbt[parent_index]
      child_elm     = self.cbt[child_index]

      #--> swap parent with child if parent bigger than child
      #defense function
      if parent_elm is None or child_elm is None:
        return

      if int(parent_elm) > int(child_elm):
        self.cbt[parent_index]  = child_elm
        self.cbt[child_index]   = parent_elm
        child_index = parent_index
      
      else:
        break

  #--> sweet function to get the pattern of sweetnes 
  def sweet(self):
    #-->defense function
    if not self.is_empty():
      parent_elm        = self.cbt[0]
      child_elm         = self.cbt[1]
      
    #--pattern of sweetnes get 1*least elm + 2*2nd least elm
    #defense function
    if parent_elm is None or child_elm is None:
      return None
    sweet_value = 1 * parent_elm + 2 * child_elm

    self.cbt.remove(parent_elm)
    self.cbt.remove(child_elm)
    self.next_index   -= 2
    return sweet_value

  
  #--> get_mini_value defention
  def get_mini_value(self):
    #-->defense function
    if self.is_empty():
      return "Complete binary tree is empty"
    return self.cbt[0]

  #--> check if array is empty
  def is_empty(self):
    return self.next_index == 0

  #--> get size of array
  def size(self):
    return len(self.cbt)

  #--> check if parent have child
  def check_child(self):
    parent_index = (self.next_index -1) // 2
    child_index   = 2*parent_index + 1
    return self.cbt[child_index]

  #--> print heap
  def __str__(self):
    #-->defense function
    if self.is_empty():
      return "Complete binary tree is empty"
    
    return " ".join([str(i) for i in self.cbt])


def cookies(K,A):
  #defense function
  if K is None or A is None:
    return None

  #basic variables
  heap        = MiniHeap(len(A))
  operations  = 0

  for data in A:
    heap.insert(data)
  
  
  #--> to check MiniHeap
  #defense function
  while heap.get_mini_value() <= int(K):
    data = heap.sweet()
    heap.insert(data)
    operations += 1

    if data is None:
      break
  print(heap.get_mini_value())
  if int(heap.get_mini_value()) >= int(K):
    return operations
  return -1

if __name__ == "__main__":
    nk = input()
    n = nk.split()[0]
    K = nk.split()[1]
    A = list(map(int, input().rstrip().split()))
    result = cookies(K,A)
    print(result)
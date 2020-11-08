#!/usr/bin/env python

#-->Create Stack class
class Stack:
  def __init__(self):
    self.arr    = []

  #-->insert elements
  def insert(self, value):
    self.arr.append(value)

  #-->pop elements
  def remove(self):
    return self.arr.pop()

#-->Create Queue Class
class Queue:
  def __init__(self):
    self.list    = []

  def enq(self, value):
    #-->basic variables
    stack1  = Stack()
    stack2  = Stack()

    #-->insert value in stack 1
    stack1.insert(value)
    
    #-->pop value from stack1 and insert in stack2
    stack2.insert(stack1.remove())
    # #-->get value from stack2 and enqueue in list
    self.list.append(stack2.remove())

  #--> return with first element
  def deq(self):
    return self.list.pop(0)

  #--> print head in Queue class
  def __str__(self):
    return str(self.list[0])


if __name__ == "__main__":
    n       = int(input())
    result  = []
    queue   = Queue()

    for i in range(n):
      q = input()
      q = q.split(" ")
      
      result.append(q)

    for elm in result:
      if elm[0] == "1":
        query, value = elm
        queue.enq(value)
      
      elif elm[0] == "2":
        queue.deq()

      elif elm[0] == "3":
        print("result is:", queue, end="\n")
      
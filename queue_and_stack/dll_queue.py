import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue: #fifo
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
      #enqueue equivalent of add_to_head
      # new_queue_node = DoublyLinkedList(value)
      if self.size == 0:
       return 
      else:
        self.storage.add_to_head(value)
        self.size = self.storage.length
    
  
    def dequeue(self):
      #equates to pop_from_tail
      if self.size == 0:
        return 
      self.storage.remove_from_tail()
      self.size = self.storage.length
      

    def len(self):
      return self.size
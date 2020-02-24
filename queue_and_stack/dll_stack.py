import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack: #lifo
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
      if self.size == 0: 
        return 
      else: 
        self.storage.add_to_head(value)
        self.size = self.storage.length

    def pop(self):
      if self.size == 0: 
        return
      self.storage.remove_from_head()
      self.size = self.storage.length
        

    def len(self):
      return self.size 

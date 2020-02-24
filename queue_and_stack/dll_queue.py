import sys
# sys.path.append('../doubly_linked_list')
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
      #enqueue equivalent of add_to_head
      new_queue_node = DoublyLinkedList(value)
      if self.size == 0:
       return new_queue_node
      else:
        self.add_to_head(new_queue_node)
    
    def dequeue(self):
      #equates to pop_from_tail
      if self.size == 0:
        return 
      self.remove_from_tail()
      

    def len(self):
      
        pass

from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
      self.limit = limit
      self.length = 0
      self.storage = DoublyLinkedList()
      self.cache = {}
      

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
      if key not in self.cache: 
        return None
      elif self.length > 0 and key in self.cache:
        self.storage.move_to_end(self.cache[key]) # most-recently used
        return key
          

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
      #if the key already exists in cache
      if key in self.cache: 
        self.storage.move_to_end(self.cache[key])
        #overwrite old value with newly specified value
        self.cache[key].value = value
      
      #if the cache is at max capacity
      elif self.length == self.limit:
       deleted_key = self.storage.remove_from_head()
       for key, value in self.cache.items():
         if value.value != deleted_key:
           self.storage.add_to_tail(value)
           self.cache[key] = self.storage.tail
      
      #else key does not exist and there is no max capacity
      else:
        self.storage.add_to_tail(value)
        self.cache[key] = self.storage.head
        self.length += 1     
        
  
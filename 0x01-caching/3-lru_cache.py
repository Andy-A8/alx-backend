#!/usr/bin/python3
"""
    Create a class LRUCache that inherits from BaseCaching and
    is a caching system:

    You must use self.cache_data - dictionary from the parent class
    BaseCaching
    You can overload def __init__(self): but don’t forget to call
    the parent init: super().__init__()
    def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value
    for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher
    than BaseCaching.MAX_ITEMS:
    you must discard the least recently used item (LRU algorithm)
    you must print DISCARD: with the key discarded and following by a new line
    def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data,
    return None
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that implements a caching system
    using the Least Recently Used (LRU) algorithm.
    """
    def __init__(self):
        """ Initialize the LRUCache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and mark as recently used
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            # Check if we need to discard an item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as recently used
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]

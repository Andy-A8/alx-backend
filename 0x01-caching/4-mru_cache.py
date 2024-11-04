#!/usr/bin/python3
"""
    Create a class MRUCache that inherits from BaseCaching and is a
    caching system:

    You must use self.cache_data - dictionary from the parent class
    BaseCaching
    You can overload def __init__(self): but don’t forget to call
    the parent init: super().__init__()
    def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value
    for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher than
    BaseCaching.MAX_ITEMS:
    you must discard the most recently used item (MRU algorithm)
    you must print DISCARD: with the key discarded and following by a new line
    def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data,
    return None
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that implements a caching system
    using the Most Recently Used (MRU) algorithm.
    """
    def __init__(self):
        """ Initialize the MRUCache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            # Update the order to mark it as most recently used
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            # Add the new item
            self.cache_data[key] = item
            self.order.append(key)  # Mark it as recently used

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the order to mark it as most recently used
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]

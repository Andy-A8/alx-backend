#!/usr/bin/python3
"""
    Create a class FIFOCache that inherits from BaseCaching and
    is a caching system:

    You must use self.cache_data - dictionary from
    the parent class BaseCaching
    You can overload def __init__(self): but don’t forget to call
    the parent init: super().__init__()
    def put(self, key, item):
    Must assign to the dictionary self.cache_data
    the item value for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher than
    BaseCaching.MAX_ITEMS:
    you must discard the first item put in cache (FIFO algorithm)
    you must print DISCARD: with the key discarded and following by a new line
    def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data,
    return None.
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the FIFOCache"""
        super().__init__()
        self.order = []  # List to keep track of the order of keys

    def put(self, key, item):
        """Assign item to the cache_data dictionary with the given key"""
        if key is None and item is None:
            pass
        else:
            """If the cache exceeds the limit, remove the oldest(first) item"""
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))

            self.cache_data[key] = item  # Add new item to the cache
            self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache using the given key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

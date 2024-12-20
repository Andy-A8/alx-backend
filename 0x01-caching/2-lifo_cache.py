#!/usr/bin/python3
"""
    Create a class LIFOCache that inherits from BaseCaching
    and is a caching system:

    You must use self.cache_data - dictionary from the parent class
    BaseCaching
    You can overload def __init__(self): but don’t forget to call
    the parent init: super().__init__()
    def put(self, key, item):
    Must assign to the dictionary self.cache_data the item
    value for the key key
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher
    than BaseCaching.MAX_ITEMS:
    you must discard the last item put in cache (LIFO algorithm)
    you must print DISCARD: with the key discarded and following by a new line
    def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data,
    return None
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the LIFOCache """
        super().__init__()
        self.order = []  # List to keep track of the order of keys

    def put(self, key, item):
        """ Add an item to the cache.
        If the cache exceeds the limit, discard the last item
        """
        if key is not None and item is not None:
            # If the cache exceeds the limit, remove the last item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop()
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item  # Add the new item to the cache
            self.order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache using the given key. """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

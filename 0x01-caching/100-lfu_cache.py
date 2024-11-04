#!/usr/bin/python3
"""
    Create a class LFUCache that inherits from BaseCaching and is a
    caching system:

    You must use self.cache_data - dictionary from the parent class
    BaseCaching
    You can overload def __init__(self): but don’t forget to call
    the parent init: super().__init__()
    def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value
    for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher that
    BaseCaching.MAX_ITEMS:
    you must discard the least frequency used item (LFU algorithm)
    if you find more than 1 item to discard, you must use the LRU algorithm
    to discard only the least recently used
    you must print DISCARD: with the key discarded and following by a new line
    def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data,
    return None
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that implements a caching system
    using the Least Frequently Used (LFU) algorithm.
    """

    def __init__(self):
        """ Initialize the LFUCache"""
        super().__init__()
        self.freq_map = {}  # Dictionary to count the frequency of each key
        # List to track the order of keys for LRU within the same frequency
        self.use_order = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq_map[key] += 1
            self.use_order.remove(key)  # Update LRU order
            self.use_order.append(key)   # Add to the end for LRU tracking
        else:
            # If adding a new item, check if we need to discard an item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item(s)
                min_freq = min(self.freq_map.values())
                lfu_keys = [k for k, v in self.freq_map.items() if v == min_freq]

                """ If there are multiple candidates, apply LRU to
                decide which to discard
                """
                lfu_key = None
                for key in self.use_order:
                    if key in lfu_keys:
                        lfu_key = key
                        break

                # Discard the LFU item
                if lfu_key:
                    del self.cache_data[lfu_key]
                    del self.freq_map[lfu_key]
                    self.use_order.remove(lfu_key)
                    print(f"DISCARD: {lfu_key}")

            # Add the new item
            self.cache_data[key] = item
            self.freq_map[key] = 1  # Frequency is 1 for a new item
            self.use_order.append(key)  # Mark as recently used

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and LRU order
        self.freq_map[key] += 1
        self.use_order.remove(key)
        self.use_order.append(key)

        return self.cache_data[key]

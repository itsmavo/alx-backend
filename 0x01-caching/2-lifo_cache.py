#!/usr/bin/env python3
""" implements LIFOCache from BaseCaching """

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ Defines LIFO cache """
    def __init__(self):
        """ Inits Class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Stores key, value pair """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[-1]))
                del self.cache_data[self.order[-1]]
                del self.order[-1]
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Returns value linked to specific key """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None

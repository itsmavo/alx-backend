#!/usr/bin/env python3

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ Creates FIFO caching system """

    def __init__(self):
        """ inits the class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ store k,v pair """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Return value linked to a specific key"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None

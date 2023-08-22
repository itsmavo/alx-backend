#!/usr/bin/env python3
""" Builds Class BasicCache """

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    Class caches information in key-value pairs
    Methods:
    put(key, item) - stores k,v pair
    get(key) - retrieves value with assoc key
    """
    def __init__(self):
        """ Inits parent class """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ Stores k,v pair """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns value linked to specific key """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None

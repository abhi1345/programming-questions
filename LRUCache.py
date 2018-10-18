from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: 
            return -1
        
        value = self.cache[key]
        self.cache.move_to_end(key)
        return value

    def put(self, key, value):
        if key in self.cache: 
            del self.cache[key]
        
        self.cache[key] = value
        
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)
               


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

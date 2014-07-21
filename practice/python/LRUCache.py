class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # last used keys order as [oldest,...,newest]
        self.lastusedkeys = []
        self.cache = {}    
        self.capacity = capacity
        self.full = 0

 
    # @return an integer
    def get(self, key):
        if not self.cache.has_key(key):
            return -1
        self.lastusedkeys.remove(key)
        self.lastusedkeys.append(key)
        return self.cache[key]
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.get(key) == -1:
            if self.full == self.capacity:
                oldest = self.lastusedkeys.pop(0)
                del self.cache[oldest]
                self.cache[key] = value
                self.lastusedkeys.append(key)
            else:
                self.cache[key] = value
                self.lastusedkeys.append(key)
                self.full += 1
        else:
            self.cache[key]=value

    def print_lastused(self):
        print self.lastusedkeys
        print self.cache

if __name__ == "__main__":
    cache = LRUCache(4)
    cache.set(2,1)
    cache.print_lastused()
    cache.set(3,2)
    cache.print_lastused()
    cache.get(2)
    cache.print_lastused()
    print cache.get(7)
    cache.set(7,1)
    cache.set(8,1)
    cache.set(9,1)
    cache.set(4,1)
    cache.set(5,1)
    cache.print_lastused()
    cache.set(7,1)
    cache.print_lastused()
    cache.set(7,4)

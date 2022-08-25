class LRUCache:

    def __init__(self, capacity: int):
        self.stack = []
        self.d = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self.stack.remove(key)
            self.stack.append(key)
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.stack.remove(key)
            self.stack.append(key)
            self.d[key] = value
        else:
            if len(self.d) == self.capacity:
                lru = self.stack.pop(0)
                self.d.pop(lru)
            self.stack.append(key)
            self.d[key] = value
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
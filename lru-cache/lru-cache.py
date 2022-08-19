class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.stack = []

    def get(self, key: int) -> int:
        if key in self.d:
            self.queue.remove(key)
            self.queue.append(key)
            return self.d[key]
        return -1

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
            if len(self.stack) == self.capacity:
                lru = self.stack.pop(0)
                self.d.pop(lru)
            self.d[key] = value
            self.stack.append(key)
            
            
            
            
            
            
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
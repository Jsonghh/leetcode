from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        ans = self.d[key]
        del self.d[key]
        self.d[key] = ans
        return ans
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
        
        if len(self.d) == self.capacity:
            del self.d[list(self.d.keys())[0]]
            
        self.d[key] = value
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
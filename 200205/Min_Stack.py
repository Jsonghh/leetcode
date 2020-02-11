import heapq
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        min_num = x if not self.stack else min(self.stack[-1][1], x)
        self.stack.append((x, min_num))
        

    def pop(self) -> None:
        if not self.stack:
            return
        num, _ = self.stack.pop()
        return num
        

    def top(self) -> int:
        if not self.stack:
            return float('-inf')
        
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        if not self.stack:
            return float('-inf')
        
        return self.stack[-1][1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
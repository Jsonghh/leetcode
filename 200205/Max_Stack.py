class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.all_num, self.max_pos = [], []

    def push(self, x: int) -> None:
        self.all_num.append(x)
        
        if not self.max_pos or x >= self.max_pos[-1][1]:
            self.max_pos.append((len(self.all_num) - 1, x))
        

    def pop(self) -> int:
        if not self.all_num:
            return float('-inf')
        
        if len(self.all_num) - 1 == self.max_pos[-1][0]:
            self.max_pos.pop()
            
        return self.all_num.pop()
        

    def top(self) -> int:
        if not self.all_num:
            return float('-inf')
        return self.all_num[-1]
        

    def peekMax(self) -> int:
        if not self.max_pos:
            return float('-inf')
        return self.max_pos[-1][1]

    def popMax(self) -> int:
        if not self.max_pos:
            return float('-inf')
        
        pos, max_num = self.max_pos.pop()
        self.all_num.pop(pos)
        
        for i in range(pos, len(self.all_num)):
            if not self.max_pos or self.all_num[i] >= self.max_pos[-1][1]:
                self.max_pos.append((i, self.all_num[i]))
                
        return max_num
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
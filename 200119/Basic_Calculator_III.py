class Solution:
    def calculate(self, s: str) -> int:
        order = {'*': 1, '/': 1, '+': 0, '-': 0}
        stack, num = [], 0
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            if c in '+-*/':
                while stack and stack[-1] != '(' and order[stack[-1]] >= order[c]:
                    op = stack.pop()
                    pre_num = stack.pop()
                    num = self.helper(pre_num, num, op)
                stack.append(num)
                stack.append(c)
                num = 0
            
            if c == '(':
                stack.append(c)
                
            if c ==')':
                while stack[-1] != '(':
                    op = stack.pop()
                    pre_num = stack.pop()
                    num = self.helper(pre_num, num, op)
                stack.pop()
                
            
                
        while stack:
            op = stack.pop()
            pre_num = stack.pop()
            num = self.helper(pre_num, num, op)
        return num
    
    def helper(self, pre_num, num, op):
        if op == '+':
            return pre_num + num
        if op == '-':
            return pre_num - num
        if op == '*':
            return pre_num * num
        if op == '/':
            return pre_num // num


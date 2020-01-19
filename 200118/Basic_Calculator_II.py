class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        num = 0
        sign = '+'

        for idx, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in '+-*/' or idx == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    stack.append(int(stack.pop() / num))
                    
                sign = char
                num = 0
                
        return sum(stack)
                    
                
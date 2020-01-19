class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        stack = [-1]
        max_len = 0
        for idx, val in enumerate(list(s)):
            if val == '(':
                stack.append(idx)
                
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    cur_len = idx - stack[-1]
                    max_len = cur_len if cur_len > max_len else max_len
                    
        return max_len
                    
        
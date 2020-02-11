class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        invalid_idx = set()
        stack = []
        for idx, c in enumerate(s):
            if c not in '()':
                continue
                
            if c == '(':
                stack.append(idx)
                
            elif not stack:
                invalid_idx.add(idx)
                
            else:
                stack.pop()
                
        invalid_idx |= set(stack)
        
        ans = ''
        for idx, c in enumerate(s):
            if idx not in invalid_idx:
                ans += c
        return ans


        
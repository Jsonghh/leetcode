class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s
    
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
                continue
            
            strs = []
            
            while stack and stack[-1] != '[':
                strs.append(stack.pop())
#             pop out '['
            stack.pop()
            
            rp_cnt, base = 0, 1
            while stack and stack[-1].isdigit():
                rp_cnt += int(stack.pop()) * base
                base *= 10
            stack.append(''.join(reversed(strs)) * rp_cnt)

            
        return ''.join(stack)
                
                
        
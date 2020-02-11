class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if not stack or ch != stack[-1][0]:
                stack.append((ch, 1))
                
            else:
                pre_ch, pre_t = stack.pop()
                if pre_t + 1 != k:
                    stack.append((ch, pre_t + 1))
                
        ans = ''
        for ch, t in stack:
            ans += ch * t
            
        return ans
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        match = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in '([{':
                stack.append(c)
            elif not stack or match[c] != stack.pop():
                return False
        return not stack
        
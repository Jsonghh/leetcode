class Solution:
    def __init__(self):
        self.mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        self.helper(digits, '', ans)
        return ans
    
    
    def helper(self,digits, cur, ans):
        if not digits:
            ans.append(cur)
            return
        d = digits[0]
        for c in self.mapping[d]:
            cur += c
            self.helper(digits[1:], cur, ans)
            cur = cur[:-1]
        return
        
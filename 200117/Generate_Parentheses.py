class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        ans = []
        self.helper(n, n, '', ans)
        return ans
    
    
    def helper(self, l, r, cur, ans):
        if l > r:
            return
        if l == 0 and r == 0:
            ans.append(cur)
            return
        if l > 0:
            self.helper(l - 1, r, cur + '(', ans)
        if r > 0:
            self.helper(l, r - 1, cur + ')', ans)
        return
            
        
        
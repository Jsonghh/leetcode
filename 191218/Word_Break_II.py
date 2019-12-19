'''
Memorization Search
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = self.helper(s, wordDict,{})
        return ans
    
    
    def helper(self, s, d,memo):
        
        if not s:
            return []
        
        if s in memo:
            return memo[s]
        
        partitions = []
        for i in range(len(s)):
            prefix = s[:i + 1]
            if prefix not in d:
                continue
            sub_par = self.helper(s[i + 1:], d,memo)
            for sub in sub_par:
                partitions.append(prefix + ' ' + sub)
        if s in d:
            partitions.append(s)
        memo[s] = partitions
        return partitions
        
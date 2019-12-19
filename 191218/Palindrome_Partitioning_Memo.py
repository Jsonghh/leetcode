class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        return self.helper(s, {})
        
        
    def helper(self, s, memo):
        if not s:
            return []
        
        if s in memo:
            return memo[s]
        
        partitions = []
        for i in range(len(s)):
            prefix = s[:i + 1]
            if not self.is_palin(prefix):
                continue
            sub_par = self.helper(s[i + 1:], memo)
            for sub in sub_par:
                partitions.append([prefix] + sub[:])
        if self.is_palin(s):
            partitions.append([s])
        memo[s] = partitions
        return partitions
        
        
    def is_palin(self, s):
        return s == s[::-1]

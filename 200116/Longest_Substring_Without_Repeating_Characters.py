class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, ans = len(s), 0
        hi, visited = 0, set()
        
        for lo in range(len(s)):
            while hi < n and s[hi] not in visited:
                visited.add(s[hi])
                hi += 1
            ans = max(ans, hi - lo)
            visited.remove(s[lo])
            
        return ans


        
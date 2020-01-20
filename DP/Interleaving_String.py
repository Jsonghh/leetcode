class Solution:
    
    def isInterleave(self, s1, s2, s3) -> bool:
        
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False
        if m == 0 or n == 0: 
            return s1 == s3 or s2 == s3
        
        dp = [True] + [False for _ in range(n)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[j] = dp[j] and s1[i-1] is s3[i+j-1] or dp[j-1] and s2[j-1] is s3[i+j-1]

        return dp[n]


'''
https://leetcode.com/problems/interleaving-string/solution/
'''
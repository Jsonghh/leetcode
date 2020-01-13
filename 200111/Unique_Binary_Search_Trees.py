class Solution:
    def numTrees(self, n: int) -> int:
        cnt = {
            0: 1,
            1: 1
        }
        self.helper(n, cnt)
        return cnt[n]
    
    def helper(self, n, cnt):
        if n in cnt:
            return cnt[n]
        cnt_ = 0
        for k in range(1, n + 1):
            cnt_ += self.helper(k - 1, cnt) * self.helper(n - k, cnt)
        cnt[n] = cnt_
        return cnt[n]
            
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if not weights:
            return -1
        
        left, right = max(weights), sum(weights)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.is_within_D(mid, weights, D):
                right = mid
            else:
                left = mid
        if self.is_within_D(left, weights, D):
            return left
        return right
    
    
    def is_within_D(self, limit, weights, d):
        cnt, cur = 1, 0
        for w in weights:
            if cur + w > limit:
                cnt += 1
                cur = 0
            cur += w
        return cnt <= d

        
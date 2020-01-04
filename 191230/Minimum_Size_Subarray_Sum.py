from collections import Counter, defaultdict
class Solution:
    def findShortestSubArray(self, nums):
        if not nums:
            return 0
        counter = dict(Counter(nums))
        nums_degree = max(counter.values())
        running_cnt = defaultdict(int)
        l, r, min_len  = 0, 0, len(nums)
        for l in range(len(nums)):
            while not running_cnt or \
                r < len(nums) and max(running_cnt.values()) < nums_degree:
                running_cnt[nums[r]] += 1
                r += 1
            if max(running_cnt.values()) == nums_degree:
                min_len = min(min_len, r - l)
            running_cnt[nums[l]] -= 1
                
        print(nums_degree, r)
        return min_len
            
        
    
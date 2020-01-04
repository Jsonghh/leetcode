from collections import Counter
class Solution:
    def findShortestSubArray(self, nums):
        if not nums:
            return 0
        nums_degree = self.find_degree(nums, 0, len(nums) - 1)
        l, r, min_len  = 0, 0, len(nums)
        for l in range(len(nums)):
            while r < len(nums) and self.find_degree(nums, l, r) < nums_degree:
                r += 1
            if self.find_degree(nums, l, r) == nums_degree:
                min_len = min(min_len, r - l + 1)
        print(nums_degree, r)
        return min_len
            
        
    def find_degree(self, nums, l, r):
        counter = Counter(nums[l : r + 1])
        degree = max(counter.values())
        return degree
        
print(Solution().findShortestSubArray([1,2,2,3,1,4,2]))
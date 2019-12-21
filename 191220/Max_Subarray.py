class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        min_sum, max_sum = 0, float('-inf')
        for num in nums:
            prefix += num
            max_sum = max(max_sum, prefix - min_sum)
            min_sum = min(prefix, min_sum)
        return max_sum
        
        
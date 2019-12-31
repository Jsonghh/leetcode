class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#         if not nums:
#             return 0
        
        min_window = len(nums) + 1
        l, r = 0, 0
        running_sum = 0
        for l in range(len(nums)):
            while r < len(nums) and running_sum < s:
                running_sum += nums[r]
                r += 1
            if running_sum >= s and r - l < min_window:
                min_window = r - l
            running_sum -= nums[l]
            
        return min_window if min_window != len(nums) + 1 else 0
            
            
        
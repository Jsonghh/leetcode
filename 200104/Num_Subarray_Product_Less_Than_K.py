class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        running_pro, i, ans = 1, 0, 0
        for j, num in enumerate(nums):
            running_pro *= num
            while running_pro >= k and i <= j:
                running_pro //= nums[i]
                i += 1
            ans += j - i + 1
        return ans
                
        
        
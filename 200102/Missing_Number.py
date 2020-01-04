class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                return nums[i - 1] + 1
            
        return nums[-1] + 1

'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
#         0 -> n, missing one number
#       expected last number n = len(nums), number of nums N = len(nums) + 1
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
'''
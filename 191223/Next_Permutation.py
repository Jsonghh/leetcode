class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if list(reversed(nums)) == sorted(nums):
            nums.sort()
            return
            
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]: 
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        left, right = i, len(nums) - 1
                        while left < right:
                            nums[left], nums[right] = nums[right], nums[left]
                            left, right = left + 1, right - 1
                        return
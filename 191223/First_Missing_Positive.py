class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums):
                i += 1
                continue
            if nums[i] == nums[nums[i] - 1]:
                i += 1
                continue
            if nums[i] == i + 1:
                i += 1
                continue

            num1, num2 = nums[i], nums[nums[i] - 1]
            nums[i], nums[num1 - 1] = num2, num1

        print(nums)  
        for i in range(len(nums)):
            if nums[i] != i + 1:
                
                return i + 1
                   
        return len(nums) + 1
                
        
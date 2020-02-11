class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.helper(0, len(nums) - 1, nums)
        return nums
        
        
        
    def helper(self, left, right, nums):
        if left >= right:
            return
        
        start, end = left, right
        pivot = nums[(left + right) // 2]
        while start <= end:

            # '=' ensures nums[start] that less than pivot will not go to the rigth part of partition
            while start <= end and nums[start] < pivot:
                start += 1
            while start <= end and nums[end] > pivot:
                end -= 1
                
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
                
        self.helper(left, end, nums)
        self.helper(start, right, nums)
                
                
            
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow, fast = 0, 0
        while fast < len(nums):
            while 0 < fast < len(nums) and nums[fast] == nums[fast - 1]:
                fast += 1
            if fast >= len(nums):
                break
            nums[slow] = nums[fast]
            slow, fast = slow + 1, fast + 1
        return slow
        
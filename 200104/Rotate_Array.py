class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
        
        k %= len(nums)
        
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        return
        
    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
        return


'''
modify sliced values
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]

'''

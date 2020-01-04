class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return float('-inf')
        
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid + 1]:
                if nums[mid] >= nums[-1]:
                    l = mid
                else:
                    r = mid
            else:
                return nums[mid + 1]
            
        if nums[l] < nums[r]:
            return nums[l]
        return nums[r]
                
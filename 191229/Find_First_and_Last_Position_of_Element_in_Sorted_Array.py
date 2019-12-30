class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        if nums[l] == target:
            left_idx = l
        elif nums[r] == target:
            left_idx = r
        else:
            return [-1, -1]
        
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        if nums[r] == target:
            right_idx = r
        else:
            right_idx = l
        return [left_idx, right_idx]
        
        
            
        
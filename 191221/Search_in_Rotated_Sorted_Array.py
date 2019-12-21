class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                if nums[mid] < nums[0] and target >= nums[0]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] >= nums[0] and target < nums[0]:
                    l = mid
                else:
                    r = mid
                
                    
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        else:
            return -1
                        
                    
            
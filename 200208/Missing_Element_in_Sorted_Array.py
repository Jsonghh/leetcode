class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing_num = None
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                continue
            
            dist = nums[i] - nums[i - 1]
            for d in range(1, dist):
                missing_num = nums[i - 1] + d
                k -= 1
                if k == 0:
                    return missing_num
                
        return nums[-1] + k
        
        
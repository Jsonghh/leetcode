class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
#       all positives, all neg
        res1 = nums[-1] * nums[-2] * nums[-3]
    
#       one or two neg
        res2 = nums[-1] * nums[0] * nums[1]
    
        return max(res1, res2)
    
    
        
        
        
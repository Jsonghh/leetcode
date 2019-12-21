class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        prefix_pro = [1]
        for num in nums[:-1]:
            prefix_pro.append(prefix_pro[-1] * num)
            
        accu_pro = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix_pro[i] *= accu_pro
            accu_pro *= nums[i]
            
        return prefix_pro
            
        
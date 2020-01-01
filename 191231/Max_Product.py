class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        max_product = nums[0]
        running_pro, running_pro_min = 1, 1
        for num in nums:
            
            running_pro, running_pro_min = max(num, num * running_pro, num * running_pro_min), \
                min(num, num * running_pro, num * running_pro_min)
            max_product = max(max_product, running_pro, running_pro_min)
        return max_product
        

print(Solution().maxProduct([-3,-4,-2]))
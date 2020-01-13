class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
#       use two pointer to do the partition
        l, r, idx = 0, len(nums) - 1, 0
        while idx <= r:
            if nums[idx] == 1:
                idx += 1
            elif nums[idx] == 0:
                # if nums[l] == 0:
                #     l, idx = l + 1, idx + 1
                #     continue
                nums[idx], nums[l] = nums[l], nums[idx]
                l, idx = l + 1, idx + 1
            else:
                # if nums[r] == 2:
                #     r = r - 1
                #     continue
                nums[idx], nums[r] = nums[r], nums[idx]
                r = r - 1
                
'''
 class Solution:
    def sortColors(self, nums: List[int]) -> None:
       
        if not nums:
            return
        
#       use two pointer to do the partition
        l, r, idx = 0, len(nums) - 1, 0
        while idx <= r:
            if nums[idx] == 1:
                idx += 1
            elif nums[idx] == 0:
                if nums[l] != 0:  
                    nums[idx], nums[l] = nums[l], nums[idx]
                l, idx = l + 1, idx + 1
            else:
                if nums[r] != 2:
                    nums[idx], nums[r] = nums[r], nums[idx]
                r = r - 1
                
            
 '''           
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        cnt = 0  
        
        if k < 0:
            return 0
              
        if k == 0:
            counter = Counter(nums)
            for freq in counter.values():
                if freq > 1:
                    cnt += 1
            return cnt
            
        index = {}
        nums = set(nums)
        for idx, num in enumerate(nums):
            another = [num + k, num - k]
            for ano in another:
                if ano in index:
                    cnt += 1
            
            index[num] = idx
        return cnt
                
                       
'''
Two Points Solution (Sliding Window)

        nums.sort()
        
        numOfPairs = 0
        
        i, j = 0, 1
        while j < len(nums):
            
            if nums[j] - nums[i] > k:
                i += 1 
            elif nums[j] - nums[i] < k:
                j += 1 
            else:
                numOfPairs += 1 
                i, j = i+1, j+1 
                while j < len(nums) and nums[j] == nums[j-1]:
                    j += 1 
                while i < j and nums[i] == nums[i-1]:
                    i += 1 
            if j == i:
                j += 1
                    
        return numOfPairs
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         use negative sign to denote visited number
        for num in nums:
            if nums[abs(num) - 1] > 0:
                
                nums[abs(num) - 1] *= -1
        ans = []        
        for idx, num in enumerate(nums):
            if num > 0:
                ans.append(idx + 1)
                
        return ans



'''
# using extra space to record visited numbers
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        visited = set()
        ans = []
        for num in nums:
            visited.add(num)
            
        for num in range(1, len(nums) + 1):
            if num not in visited:
                ans.append(num)
        return ans
'''
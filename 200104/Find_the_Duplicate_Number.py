class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        tortoise, hare = nums[0], nums[0]
        while True:
            tortoise, hare = nums[tortoise], nums[nums[hare]]
            if tortoise == hare:
                break
        
        p1, p2 = nums[0], tortoise
        while p1 != p2:
            p1, p2 = nums[p1], nums[p2]
            
        return p1
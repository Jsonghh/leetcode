class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        most_right = 0
        for idx, max_step in enumerate(nums):
            if idx > most_right:
                return False
            most_right = max(most_right, max_step + idx)
            
        return True
        
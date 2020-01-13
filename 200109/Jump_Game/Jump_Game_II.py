class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        most_right = most_right_prenode = 0

        for i in range(len(nums)):
            
            if i > most_right:
                step += 1
                most_right = most_right_prenode
                
            most_right_prenode = max(nums[i] + i, most_right_prenode)
            
        return step
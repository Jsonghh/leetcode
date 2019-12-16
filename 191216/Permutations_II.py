class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        ans = []
        visited = set()
        self.helper(nums, [], ans, visited)
        return ans
    
    
    def helper(self, nums, cur, ans, visited):
        if len(cur) == len(nums):
            ans.append(cur[:])
            return 
        
        for st in range(len(nums)):
            if st in visited:
                continue
            if st > 0 and nums[st] == nums[st - 1] and st - 1 not in visited:
                continue
            cur.append(nums[st])
            visited.add(st)
            self.helper(nums, cur, ans, visited)
            visited.remove(st)
            cur.pop()
        return


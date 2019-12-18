class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.helper(candidates, 0, [], ans, target)
        return ans
    
    
    def helper(self, nums, idx, cur, ans, t):
        if t == 0:
            ans.append(cur[:])
            return
        if t < 0 or idx == len(nums):
            return
 
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            cur.append(nums[i])
            self.helper(nums, i + 1, cur, ans, t - nums[i])
            cur.pop()
        return 
        
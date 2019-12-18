class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return not target
        ans = []
        self.helper(candidates, 0, [], target, ans)
        return ans
    
    
    def helper(self, nums, idx, cur, target, ans):
        if sum(cur) == target:
            ans.append(cur[:])
            return
        if sum(cur) > target:
            return
        for i in range(idx, len(nums)):
            cur.append(nums[i])
            self.helper(nums, i, cur, target, ans)
            cur.pop()
        return
        
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        nums.sort()
        ans = []
        self.helper(nums, 0, [], ans)
        return ans
    
    
    def helper(self, nums, idx, subsets, ans):
        ans.append(subsets[:])
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            subsets.append(nums[i])
            self.helper(nums, i + 1, subsets, ans)
            subsets.pop()
        return
            
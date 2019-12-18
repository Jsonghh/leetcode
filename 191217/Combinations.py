class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n or not k:
            return [[]]
        nums = [i for i in range(1, n+1)]
        ans = []
        self.helper(nums, 0, [], ans, k)
        return ans
    
    
    def helper(self, nums, idx, ss, ans, k):
        if len(ss) == k:
            ans.append(ss[:])
            return
        for i in range(idx, len(nums)):
            ss.append(nums[i])
            self.helper(nums, i + 1, ss, ans, k)
            ss.pop()
        return 
        
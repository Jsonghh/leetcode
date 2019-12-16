class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ans = []
        visited = set()
        self.helper(nums, [], ans, visited)
        return ans
    
    
    def helper(self, nums, cur, ans, visited):
        if len(cur) == len(nums):
            ans.append(cur[:])
            return 
        for num in nums:
            if num in visited:
                continue
            cur.append(num)
            visited.add(num)
            self.helper(nums, cur, ans, visited)
            visited.remove(num)
            cur.pop()
        return
        
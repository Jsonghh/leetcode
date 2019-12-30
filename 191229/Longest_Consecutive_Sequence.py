class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans, records = 0, set(nums)
        for num in nums:
            if num - 1 in records:
                continue
            higher = num + 1
            while higher in records:
                higher += 1
            ans = max(ans, higher - num)
        return ans
        
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        records = defaultdict(int)
        records[0] = 1
        ans = 0
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in records:
                ans += records[prefix_sum - k]
            
            records[prefix_sum] += 1
        return ans
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        baseline = len(nums) // 3
        ans = []
        for num, freq in counter.items():
            if freq > baseline:
                ans.append(num)
        return ans


        
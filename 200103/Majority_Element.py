from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        baseline = len(nums) // 2
        for num in counter:
            if counter[num] > baseline:
                return num
        return -1
        
        
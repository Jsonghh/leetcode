from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        for num, freq in counter.items():
            if freq != 2:
                return num
            
        return float('-inf')
        
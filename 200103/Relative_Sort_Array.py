from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if not arr1 or not arr2:
            return []
        ans = []
        counter_1 = Counter(arr1)
        for num in arr2:
            for i in range(counter_1[num]):
                ans.append(num)
        arr1.sort()
        for num in arr1:
            if num not in arr2:
                ans.append(num)
        return ans
                
        
        
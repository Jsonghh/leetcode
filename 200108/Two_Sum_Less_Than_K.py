class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        l, r = 0, len(A) - 1
        max_sum = -1
        while l < r:
            cur_sum = A[l] + A[r]
            if cur_sum < K:
                l += 1
                if max_sum < cur_sum:
                    max_sum = cur_sum
            else:
                r -= 1
        return max_sum
            
            
            



'''
Brute Force Solution

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        cur_sum = -1
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] < K and A[i] + A[j] > cur_sum:
                    cur_sum = A[i] + A[j]
        return cur_sum
        
'''
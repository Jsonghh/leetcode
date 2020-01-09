class Solution(object):
    def findLength(self, A, B):
        a, b = sorted([A, B], key=len)
        m, n = len(a), len(b)
        ans = 0
        for pointer in range(-m + 1, m + n - 1):
            cnt = 0
            for idx_a in range(m):
                idx_b = pointer + idx_a
                if idx_b < 0:
                    continue
                if idx_b >= m:
                    break
                if a[idx_a] == b[idx_b]:
                    cnt += 1
                    if cnt > ans: ans = cnt
                else:
                    cnt = 0
        return ans


'''
# Brute Force
from collections import defaultdict
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        idx_in_b = defaultdict(list)
        for i, num in enumerate(B):
            idx_in_b[num].append(i)
        
        ans = 0
        for j, num in enumerate(A):
            for i in idx_in_b[num]:
                k = 0
                while i + k < len(B) and j + k < len(A) and A[j + k] == B[i + k]:
                    k += 1
                ans = max(ans, k)
        return ans
'''
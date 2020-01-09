from collections import deque
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = deque([])
        if not A:
            return ans
        for num in A:
            if num % 2 == 1:
                ans.append(num)
            else:
                ans.appendleft(num)
        return ans


'''
Two Points Solution

class Solution(object):
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A
'''
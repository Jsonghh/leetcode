class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        cnt = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                previous_num = A[i]
                A[i] = A[i - 1] + 1
                cnt += A[i - 1] + 1 - previous_num
        return cnt
                
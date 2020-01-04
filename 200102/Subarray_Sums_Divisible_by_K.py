class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix_sum = [0]
        for i in range(len(A)):
            prefix_sum.append(prefix_sum[-1] + A[i])
            
        l, r = 0, 0
        cnt = 0
        for l in range(len(prefix_sum)):
            for r in range(l + 1, len(prefix_sum)):
                interval_sum = prefix_sum[r] - prefix_sum[l]
                if interval_sum % K == 0:
                    cnt += 1
        return cnt
        
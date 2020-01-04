class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if not A:
            return 0
        prefix_sum = 0 
        prefix_sums = []
        for i in range(len(A)):
            prefix_sum += A[i]
            prefix_sums.append(prefix_sum)
        return max(self.get_max(prefix_sums, L, M), self.get_max(prefix_sums, M, L))
        
    def get_max(self, prefix_sum, l, m):
        left_running_max = [0] * len(prefix_sum)
        i = l - 1
        left_running_max[i] = prefix_sum[i]
        left_max = prefix_sum[i]
        i += 1
        while i < len(prefix_sum) - m:
            left_max = max(prefix_sum[i] - prefix_sum[i - l], left_max)
            left_running_max[i] = left_max
            i += 1
        
        i = len(prefix_sum) - 1 - m
        right_max, max_sum = 0, 0
        while i >= 0:
            right_max = max(right_max, prefix_sum[i + m] - prefix_sum[i])
            max_sum = max(max_sum, left_running_max[i] + right_max)
            i -= 1
            
        return max_sum

            
        
         
        
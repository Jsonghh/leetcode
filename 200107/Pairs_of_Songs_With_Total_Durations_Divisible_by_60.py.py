class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res  , count  = 0,  [0] * 60
        for t in time:
            remainder = t % 60
            res += count[(60 - remainder) % 60] # %60 is for index==0
            count[remainder] += 1
        return res


'''
Brute Force Solution

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = 0
        for i in range(len(time) - 1):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    cnt += 1
        return cnt

'''


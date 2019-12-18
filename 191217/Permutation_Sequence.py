'''
康托展开
https://juejin.im/entry/5943b9c88d6d810058d49311
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
# permutation from (1, n),  2341 (1 * 4! + 1 * 3! + 1 * 1! + 0 * 0!)
        nums = [i for i in range(1, n + 1)] # i numbers that are less than nums[i]
        fac = [1]
        for i in range(1, n + 1):
            fac.append(fac[-1] * i)
        
        ans = []
        
        for i in range(n):
            quo, rem = divmod( k - 1, fac[n - i - 1])
            ans.append(nums[quo])
            del nums[quo]
            k = rem + 1
        return ''.join([str(x) for x in ans])
            
        
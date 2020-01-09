class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        pre = lower - 1
        for cur in nums + [upper + 1]:
            if cur - pre == 2:
                ans.append(str(pre + 1))
            elif cur - pre > 2:
                ans.append(str(pre + 1) + '->' + str(cur - 1))
            pre = cur
            
        return ans
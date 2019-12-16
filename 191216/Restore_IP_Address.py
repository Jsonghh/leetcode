'''
split into 4 parts, 0 - 255 for every part
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        ans = []
        self.helper(s, 0, [], ans)
        return ans
    
    
    def helper(self, s, idx, subsets, ans):
        if len(subsets) == 4 and idx == len(s):
            ans.append('.'.join(subsets))
            return
        if len(subsets) == 4:
            return
        for i in range(idx, idx + 3):
            if i == len(s):
                return
            num = s[idx : i + 1]
            if int(num) > 255 or int(num) > 0 and num[0] == '0' or int(num) == 0 and len(num) > 1:
                return
            subsets.append(num)
            self.helper(s, i + 1, subsets, ans)
            subsets.pop()
        return
        
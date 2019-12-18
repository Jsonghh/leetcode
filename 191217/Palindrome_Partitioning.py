class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        ans = []
        self.helper(s, [], ans)
        return ans
        
        
    def helper(self, s, cur_list, ans):
        if not s:
            ans.append(cur_list[:])
            return
        for i in range(len(s)):
            prefix = s[:i + 1]
            if self.is_palin(prefix):
                cur_list.append(prefix)
                self.helper(s[i + 1:], cur_list, ans)
                cur_list.pop()
        return
        
        
    def is_palin(self, s):
        return s == s[::-1]
        # l, r = 0, len(s) - 1
        # while l < r:
        #     if s[l] != s[r]:
        #         return False
        #     l, r = l + 1, r - 1
        # return True
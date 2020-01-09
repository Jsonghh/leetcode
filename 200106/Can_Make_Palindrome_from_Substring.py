'''
TLE solution


from collections import defaultdict
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        if not s:
            return True
        ans = []
        prefix_cnt = [defaultdict(int)]
        for ch in s:
            new_cnt = prefix_cnt[-1].copy()
            new_cnt[ch] = prefix_cnt[-1][ch] + 1
            prefix_cnt.append(new_cnt)
        
        for start, end, k in queries:
            ans.append(self.helper(s, start, end, k, prefix_cnt))
            
        return ans
    
    
    def helper(self, s, start, end, k, prefix_cnt):
        cur_cnt = {}
        for ch, cnt in prefix_cnt[end + 1].items():
            cur_cnt[ch] = cnt - prefix_cnt[start][ch]
            if not cur_cnt[ch]:
                del cur_cnt[ch]
            
        odd_cnt = 0
        for fre in cur_cnt.values():
            if fre % 2 == 1:
                odd_cnt += 1
        if k >= odd_cnt // 2:
            return True
        return False


    def helper(self, s, start, end, k, prefix_cnt):
        cur_cnt = Counter(s[start : end + 1])
        # for ch, cnt in prefix_cnt[end + 1].items():
        #     cur_cnt[ch] = cnt - prefix_cnt[start][ch]
        #     if not cur_cnt[ch]:
        #         del cur_cnt[ch]
            
        odd_cnt = 0
        for fre in cur_cnt.values():
            if fre % 2 == 1:
                odd_cnt += 1
        if k >= odd_cnt // 2:
            return True
        return False
                
    TLE when need to build a dictionary in the recursiong function
        
        
            
'''

from collections import defaultdict
class Solution:
    def canMakePaliQueries(self, s, queries):
        prefix_cnt = [defaultdict(int)]
        for ch in s:
            prefix_cnt.append(prefix_cnt[-1].copy())
            prefix_cnt[-1][ch] += 1
        ans = []
        for start, end, k in queries:
            ans.append(self.helper(s, start, end, k, prefix_cnt))
        return ans

    def helper(self, s, start, end, k, prefix_cnt):
        odd_cnt = 0
        for ch, freq in prefix_cnt[end + 1].items():
            cur_freq = freq - prefix_cnt[start][ch]
            odd_cnt += cur_freq % 2
        if k >= odd_cnt // 2:
            return True
        return False
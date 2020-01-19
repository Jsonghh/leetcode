from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_cnt, t_cnt = defaultdict(int), Counter(t)
        new_matched, left = 0, 0
        min_len, ans = len(s) + 1, ''
        
        for right in range(len(s)):
            new_c = s[right]
            s_cnt[new_c] += 1
            
            if new_c in t_cnt and s_cnt[new_c] <= t_cnt[new_c]:
                new_matched += 1
                
            while left <= right and new_matched == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left : right + 1]
                
                remove_c = s[left]
                left += 1
                s_cnt[remove_c] -= 1
                if remove_c in t_cnt and s_cnt[remove_c] < t_cnt[remove_c]:
                    new_matched -= 1
                    
        return ans
        
        
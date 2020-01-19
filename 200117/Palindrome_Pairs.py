class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words:
            return []
        
        idx_table, ans = {}, []
        for idx, strs in enumerate(words):
            idx_table[strs] = idx
            
        for idx, strs in enumerate(words):
            for i in range(len(strs) + 1):
                left, right = strs[: i], strs[i:]
                
                if left == left[::-1]:
                    r_right = right[::-1]
                    if r_right in words and idx_table[r_right] != idx:
                        ans.append([idx_table[r_right], idx])
                        
                if right and right == right[::-1]:
                    r_left = left[::-1]
                    if r_left in words:
                        ans.append([idx, idx_table[r_left]])
                        
        return ans
                        
        
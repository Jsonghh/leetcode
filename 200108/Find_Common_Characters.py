from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        common_frequencies = [float('inf')] * 26
        for string in A:
            counter = [0] * 26
            for ch in string:
                counter[ord(ch) - ord('a')] += 1
            for idx, freq in enumerate(counter):
                common_frequencies[idx] = min(counter[idx], common_frequencies[idx])
        ans = []
        for idx, freq in enumerate(common_frequencies):
            for _ in range(freq):
                ans.append(chr(idx + ord('a')))
                
        return ans

'''
Use Counter method and build another array to indicate whether a certain character appears in each string
from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        common_frequencies = [float('inf')] * 26
        exists = [0] * 26
        for string in A:
            counter = Counter(string)
            for ch in counter:
                idx = ord(ch) - ord('a')
                exists[idx] += 1
                common_frequencies[idx] = min(counter[ch], common_frequencies[idx])
        ans = []
        for idx, freq in enumerate(common_frequencies):
            if exists[idx] != len(A):
                continue
            for _ in range(freq):
                
                ans.append(chr(idx + ord('a')))
                
        return ans
        
        
'''
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        chrs = []
        for char, freq in counter.items():
            chrs.append((-freq, char))
            
        chrs.sort()
        
        ans = ''
        for freq_, char in chrs:
            ans += char * (-freq_)
            
        return ans


        
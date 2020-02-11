from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        fre_num = [[] for _ in range(len(words) + 1)] # index is frequency = [1, len(nums)]
        for word, freq in counter.items():
            fre_num[freq].append(word)
            fre_num[freq].sort()
            
        ans = []
        for i in range(len(fre_num))[::-1]:
            if not fre_num[i]:
                continue
            for j in range(len(fre_num[i])):
                if len(ans) < k:
                    ans.append(fre_num[i][j])
                    
        return ans
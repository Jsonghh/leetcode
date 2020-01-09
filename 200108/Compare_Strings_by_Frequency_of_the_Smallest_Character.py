class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        if not queries:
            return ans
        w_frequency = []
        for word in words:
            w_frequency.append(word.count(min(word)))
        ans = []
        for query in queries:
            cnt = 0
            qf = query.count(min(query))
            for wf in w_frequency:
                if qf < wf:
                    cnt += 1
            ans.append(cnt)
                    
        return ans
                    
        
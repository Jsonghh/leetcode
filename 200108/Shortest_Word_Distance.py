class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        min_dist = len(words)
        idx1, idx2 = -1, -1
        for i, string in enumerate(words):
            if string == word1:
                idx1 = i
            elif string == word2:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                min_dist = min(min_dist, abs(idx1 - idx2))
        return min_dist
        
        
'''
Using extra space
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = [], []
        for idx, string in enumerate(words):
            if string == word1:
                idx1.append(idx)
            elif string == word2:
                idx2.append(idx)
        min_dist = len(words)
        for iidx1 in idx1:
            for iidx2 in idx2:
                cur_dist = abs(iidx1 - iidx2)
                if cur_dist < min_dist:
                    min_dist = cur_dist
        return min_dist
'''
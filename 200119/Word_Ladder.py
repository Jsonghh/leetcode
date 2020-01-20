class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        l = set(wordList)
        l.add(beginWord)
        
#         distance to the end word:
        d = {}
        d[endWord] = 1
        queue = [endWord]
        
        while queue:
            cur = queue.pop(0)
            for nw in self.nws(cur, l):
                if nw in d:
                    continue
                    
                d[nw] = d[cur] + 1
                
                if nw == beginWord:
                    return d[nw]
                
                queue.append(nw)
                
        return 0
        
        
    def nws(self, cur, l):
        aph = 'abcdefghijklmnopqrstuvwxyz'
        words = set([])
        
        for i in range(len(cur)):
            for c in aph:
                if c == cur[i]:
                    continue
                nw = cur[:i] + c + cur[i + 1:]
                
                if nw not in l:
                    continue
                    
                words.add(nw)
                
        return words
                
        
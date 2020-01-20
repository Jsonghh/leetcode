class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        d = {}
        results = []
        wordList = set(wordList)
        wordList.add(beginWord)

        self.bfs(beginWord, endWord, wordList, d)
        
        self.dfs(beginWord, endWord, wordList, d, [beginWord], results)
        
        return results
    

    # use bfs to record the distance to endWord
    def bfs(self, s, e, l, d):
        d[e] = 1
        q = [e]
        while q:
            cur = q.pop(0)
            for nw in self.fnws(cur, l):
                if nw in d:
                    continue
                d[nw] = d[cur] + 1
                q.append(nw)
    

    # use dfs to update cur_path and append valid paths to the ans
    def dfs(self, cur, e, l, d, path, results):
        if cur == e:
            results.append(list(path))
            return

        for nw in self.fnws(cur, l):
            if nw not in d or d[nw] != d[cur] - 1:
                continue
            path.append(nw)
            self.dfs(nw, e, l, d, path, results)
            path.pop()
    

    # find possbile next words according to the wordlist
    def fnws(self, w, l):
        aph = 'abcdefghijklmnopqrstuvwxyz'
        nws = []
        for i in range(len(w)):
            for c in aph:
                if c == w[i]:
                    continue
                nw  = w[:i] + c + w[i + 1:]
                if nw not in l:
                    continue
                nws.append(nw)
        return nwscd
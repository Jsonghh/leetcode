class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegrees = {ch: 0 for word in words for ch in word}
        graph = {ch: [] for word in words for ch in word}
        
        for pos in range(len(words) - 1):
            for i in range(min(len(words[pos]), len(words[pos + 1]))):
                pre, last = words[pos][i], words[pos + 1][i]
                if pre == last:
                    continue
                graph[pre].append(last)
                indegrees[last] += 1
                break
                
#         Toposort:
        queue = [ch for ch in indegrees if indegrees[ch] == 0]
        ans = []
        while queue:
            cur_ch = queue.pop(0)
            ans.append(cur_ch)
            for next_ch in graph[cur_ch]:
                indegrees[next_ch] -= 1
                if indegrees[next_ch] == 0:
                    queue.append(next_ch)
                    
        if len(ans) != len(indegrees):
            return ''
        
        return ''.join(ans)
            
                
            
        
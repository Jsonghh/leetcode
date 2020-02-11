class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for [c1, c2], val in zip(equations, values):
            graph[c1].append([c2, val])
            if val != 0:
                graph[c2].append([c1, 1/val])
        
        res = []
        for c1, c2 in queries:
            res.append(self.helper(c1, c2, graph))
        return res
    
    
    def helper(self, dividend, divisor, graph):
        if dividend not in graph or divisor not in graph:
            return -1.0
        
        stack = [(dividend, 1)]
        visited = set()
        while stack:
            num, factor = stack.pop()
            if num == divisor:
                return factor
            
            for nnum, nfactor in graph[num]:
                if nnum in visited:
                    continue
                stack.append((nnum, factor * nfactor))
                visited.add(nnum)
                
        return -1.0

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        
        ans = []
        self.helper([0], graph, 0, ans)
        return ans
    
    
    def helper(self, path, graph, start, ans):
        if not graph[start]:
            ans.append(path[:])
        
        for node in graph[start]:
            path.append(node)
            self.helper(path, graph, node, ans)
            path.pop()
        

        
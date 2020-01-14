# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def __init__(self,):
        self.g = defaultdict(set)
        
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:

        self.helper(root, root)

        queue = [node for node in self.g if node.val == k]
        visited = set(queue)
        while queue:
            node = queue.pop(0)
            
            if len(self.g[node]) == 1:
                return node.val
            
            for nei in self.g[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                queue.append(nei)
                
        return float('-inf')
        
        
    def helper(self, node, par):
        if not node:
            return
            
        self.g[node].add(par)
        self.g[par].add(node)
        self.helper(node.left, node)
        self.helper(node.right, node)
        
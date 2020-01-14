# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.d = defaultdict(list)
        self.helper(root, 0, 0)
        ans = []
        for k in sorted(self.d.keys()):
            ans.append([v[1] for v in sorted(self.d[k])])
        return ans
    
    def helper(self, node, x, y):
        if not node:
            return
        
        self.d[x].append((y, node.val))
        self.helper(node.left, x - 1, y + 1)
        self.helper(node.right, x + 1, y + 1)
        return
        
            
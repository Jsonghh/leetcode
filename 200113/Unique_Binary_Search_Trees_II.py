# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        return self.helper(1, n)
    
    def helper(self, start, end):
        if start > end:
            return [None]
        res = []
        for rootval in range(start, end + 1):
            left_trees = self.helper(start, rootval - 1)
            right_trees = self.helper(rootval + 1, end)
            for i in left_trees:
                for j in right_trees:
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
                    
            
        
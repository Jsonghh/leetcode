# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
    
        return self.dfs(root, float('inf'), float('-inf'))
    
    
    def dfs(self, node, upper, lower):
        if not node:
            return True
        
        if node.val >= upper or node.val <= lower:
            return False
        
        if not self.dfs(node.left, node.val, lower):
            return False
        
        if not self.dfs(node.right, upper, node.val):
            return False
        
        return True
        

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum = 0
        self.helper(root, L, R)
        return self.sum
    
    
    def helper(self, node, L, R):
        if not node:
            return
        
        if L <= node.val <= R:
            self.sum += node.val
        if node.val > L:
            self.helper(node.left, L, R)
        if node.val < R:
            self.helper(node.right, L, R)
            
        return
        
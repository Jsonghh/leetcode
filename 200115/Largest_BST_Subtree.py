# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0
        self.iterate(root)
        return self.ans
    
    def iterate(self, node):
        
        num, is_valid = self.is_valid(node, float('inf'), float('-inf'))
        if is_valid:
            self.ans = max(self.ans, num)
        if node.left:
            self.iterate(node.left)
        if node.right:
            self.iterate(node.right)
        
        
    def is_valid(self, node, upper, lower):
        if not node:
            return 0, True
        
        if node.val >= upper or node.val <= lower:
            return 0, False
        
        valid_nodes_left, is_left_valid = self.is_valid(node.left, node.val, lower)
        if not is_left_valid:
            return 0, False
        
        valid_nodes_right, is_right_valid = self.is_valid(node.right, upper, node.val)
        if not is_right_valid:
            return 0, False
        
        return valid_nodes_left + valid_nodes_right + 1, True
        
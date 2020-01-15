# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.min_diff = float('inf')
        self.val = None
        
        self.helper(root, target)
        return self.val
        
        
    def helper(self, node, target):
        diff = abs(node.val - target)
        if diff < self.min_diff:
            self.min_diff = diff
            self.val = node.val

        if node.val == target:
            return
        
        if node.val < target and node.right:
            self.helper(node.right, target)
            
        if node.val > target and node.left:
            self.helper(node.left, target)
            
        return
        
        
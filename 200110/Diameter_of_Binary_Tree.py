# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.diameter = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.helper(root)
        return self.diameter
    
    def helper(self, node):
        if not node:
            return 0
        left_deep, right_deep = self.helper(node.left), self.helper(node.right)
        self.diameter = max(self.diameter, left_deep + right_deep)
        return 1 + max(left_deep, right_deep)
        
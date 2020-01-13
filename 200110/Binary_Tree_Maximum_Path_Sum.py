# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    max_sum = float('-inf')
    def helper(self, node):
        cur_sum = node.val
        sumleft, sumright = 0, 0
        if node.left:
            sumleft = max(0, self.helper(node.left))
        if node.right:
            sumright = max(0, self.helper(node.right))
        cur_sum += sumleft + sumright
        self.max_sum = max(self.max_sum, cur_sum)
        return max(node.val + sumleft, node.val + sumright)
        
        
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.helper(root)
        return self.max_sum
        
    
    
        

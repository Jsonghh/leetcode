#_Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.cnt = 0
        self.check(root)
        return self.cnt
    
    def check(self, node):
        if not node:
            return True
        
        lcheck, rcheck = self.check(node.left), self.check(node.right)
        if lcheck and rcheck and (not node.left or node.left.val == node.val) \
            and (not node.right or node.right.val == node.val):
            self.cnt += 1
            return True
        return False
        
        
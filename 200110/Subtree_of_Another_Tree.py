# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s, t):    
        if not t:
            return True
        if not s:
            return t is None
        return self.equals(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def equals(self, s,t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.equals(s.left, t.left) and self.equals(s.right, t.right)
        
  
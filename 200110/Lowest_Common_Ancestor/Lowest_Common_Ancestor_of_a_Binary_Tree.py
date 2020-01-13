# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        
        found_left, found_right = self.lowestCommonAncestor(root.left, p, q), \
                                    self.lowestCommonAncestor(root.right, p, q)
        
        if found_left and found_right:
            return root
        if found_left:
            return found_left
        if found_right:
            return found_right
        return None
        


        
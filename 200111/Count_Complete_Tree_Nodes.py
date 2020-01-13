# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        depth_left, depth_right = self.get_depth(root, True), self.get_depth(root, False)
        if depth_left == depth_right:
            return 2 ** depth_left - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
    
    def get_depth(self, root, is_left):
        if not root:
            return 0
        if is_left:
            return self.get_depth(root.left, is_left) + 1
        else:
            return self.get_depth(root.right, is_left) + 1
        
        
        
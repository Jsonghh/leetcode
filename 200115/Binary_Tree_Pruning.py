# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root_contains_one = self.contains_one(root)
        if not root_contains_one: return None
        else: return root
        
        
    def contains_one(self, node):
        if not node:
            return False
        left_contains_one = self.contains_one(node.left)
        right_contains_one = self.contains_one(node.right)
        if not left_contains_one:
            node.left = None
        if not right_contains_one:
            node.right = None
            
        return node.val == 1 or left_contains_one or right_contains_one
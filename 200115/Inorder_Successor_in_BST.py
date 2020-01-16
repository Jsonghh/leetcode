# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        stack = []
        while root:
            stack.append(root)
            root = root.left
            
        while stack:
            node = stack.pop()
            if node.right:
                root = node.right
                while root:
                    stack.append(root)
                    root = root.left
            if node.val == p.val:
                return stack.pop() if stack else None
        return None
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        x = y = prev = None
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and root.val < prev.val:
                y = root
                if not x:
                    x = prev
                else:
                    break
            prev = root
            root = root.right
        x.val, y.val = y.val, x.val
        
                
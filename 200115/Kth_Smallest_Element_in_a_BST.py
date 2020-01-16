# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return root
        stack = []
        while root:
            stack.append(root)
            root = root.left
        cnt = 0    
        while stack:
            node = stack.pop()
            cnt += 1
            if cnt == k:
                return node.val
            if node.right:
                root = node.right
                
                while root:
                    stack.append(root)
                    root = root.left
                    
        return float('-inf')
            
        
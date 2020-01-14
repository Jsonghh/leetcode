# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, ans = [], []
        while root:
            stack.append(root)
            root = root.left
            
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                root = node.right
                while root:
                    stack.append(root)
                    root = root.left
        return ans
                
        
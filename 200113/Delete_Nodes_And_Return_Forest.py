# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        res = []
        root = self.helper(root, res, set(to_delete))
        if root:
            res.append(root)
            
        return res
        
        
    def helper(self, root, res, to_delete):
        if not root:
            return None
        
        root.left = self.helper(root.left, res, to_delete)
        root.right = self.helper(root.right, res, to_delete)
        
        if root.val not in to_delete:
            return root
        else:
            if root.left:
                res.append(root.left)
            if root.right:
                res.append(root.right)
            return None
        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        while root:
            leaves = []
            if self.is_leaf(root, leaves):
                leaves.append(root.val)
                root = None
            ans.append(leaves[:])
                
        return ans
    
    
    def is_leaf(self, node, leaves):
        if not node.left and not node.right:
            return True
        
        if node.left and self.is_leaf(node.left, leaves):
            leaves.append(node.left.val)
            node.left = None
            
        if node.right and self.is_leaf(node.right, leaves):
            leaves.append(node.right.val)
            node.right = None

        return False
            
        
        
        
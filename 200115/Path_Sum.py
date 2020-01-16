# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        return self.helper(root, 0, sum)
    
    def helper(self, root, cur_sum, target):
        cur_sum += root.val
        if not root.left and not root.right:
            return cur_sum == target
        found_left, found_right = False, False
        if root.left:
            found_left = self.helper(root.left, cur_sum, target)
        if root.right:
            found_right = self.helper(root.right, cur_sum, target)
        return found_left or found_right
            
        

        
        
        
        
        
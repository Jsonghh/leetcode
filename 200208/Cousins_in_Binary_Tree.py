# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        
        queue = [(root, root, 0)]
        par_x, depth_x = None, None
        par_y, depth_y = None, None
        
        while queue:
            node, par, depth = queue.pop(0)
            if node.val == x:
                par_x, depth_x = par, depth
            if node.val == y:
                par_y, depth_y = par, depth
            if par_x and par_y:
                break
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))
                
        return par_x != par_y and depth_x == depth_y
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = [root]
        max_depth = 0
        while queue:
            max_depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return max_depth
        
        
        
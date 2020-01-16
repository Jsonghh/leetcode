# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root]
        while queue:
            cur_node = queue.pop(0)
            if not cur_node:
                break
            queue.append(cur_node.left)
            queue.append(cur_node.right)
            
        for rest in queue:
            if rest:
                return False
            
        return True
            
        
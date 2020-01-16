# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self,):
        self.l = self.r = 0
        
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.helper(root, x)
        nodes_for_2 = max(self.l, self.r, n - self.l - self.r - 1)
        return nodes_for_2 > n // 2
    
    def helper(self, root, x):
        if not root:
            return 0
        l = self.helper(root.left, x)
        r = self.helper(root.right, x)
        if x == root.val:
            self.l = l
            self.r = r
        return l + r + 1
    
    
        
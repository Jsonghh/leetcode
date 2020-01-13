# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        q = [root]
        results = []
        while q:
            n = len(q)
            for i in range(n):
                cur = q.pop(0)
                if i == n - 1:
                    results.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return results
                
        
        
        
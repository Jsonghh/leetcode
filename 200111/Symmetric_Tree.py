# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = [root]
        while q:
            l, r = 0, len(q) - 1
            # check for the symmetry for the current level
            while l < r:  
                if q[l].val != q[r].val:
                    return False
                l, r = l + 1, r - 1
            # append nodes in the next level into the queue
            for i in range(len(q)):
                cur = q.pop(0)
                if cur.val == '#':
                    continue
                if cur.left:
                    q.append(cur.left)
                else:
                    q.append(TreeNode('#'))
                if cur.right:
                    q.append(cur.right)
                else:
                    q.append(TreeNode('#'))
        return True
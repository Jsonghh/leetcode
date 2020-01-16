# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        self.helper(root, [], ans)
        return ans
    
    def helper(self, node, cur, ans):
        if not node:
            return
        if not node.left and not node.right:
            cur.append(str(node.val))
            ans.append('->'.join(cur[:]))
            return
            
        cur.append(str(node.val))
        if node.left:
            self.helper(node.left, cur, ans)
            cur.pop()
            
        if node.right:
            self.helper(node.right, cur, ans)
            cur.pop()
        return 

      
        
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return ''
        stack = [(root, str(root.val))]
        ans = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                ans.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        return ans
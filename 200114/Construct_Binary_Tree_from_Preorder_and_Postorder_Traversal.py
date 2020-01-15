# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        
        
        root = self.helper(pre, post)
        return root
    
    def helper(self, pre, post):
        if not pre or not post:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        
        nodes_in_left = post.index(pre[1]) + 1
        root.left = self.helper(pre[1 : nodes_in_left + 1], post[: nodes_in_left])
        root.right = self.helper(pre[nodes_in_left + 1:], post[nodes_in_left : -1])
        
        return root
        
        
        
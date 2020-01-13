# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        left_boundary = self.get_left(root.left)
        leaves = self.get_leaves(root)
        right_boundary = self.get_right(root.right)
        
        if len(leaves) == 1:
            leaves = []
        if leaves and left_boundary:
            leaves = leaves[1:]
        if leaves and right_boundary:
            leaves = leaves[:-1]
        
        return [root.val] + left_boundary + leaves + list(reversed(right_boundary))
    
    def get_left(self, node):
        left_boundary = []
        while node:
            left_boundary.append(node.val)
            if node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                node = None
        return left_boundary
    
    def get_right(self, node):
        right_boundary = []
        while node:
            right_boundary.append(node.val)
            if node.right:
                node = node.right
            elif node.left:
                node = node.left
            else:
                node = None
        return right_boundary
    
    def get_leaves(self, node):
        stack = [node]
        leaves = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return leaves
            
        
    
    
        
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return 
        
        self.dummy = Node(-1)
        self.cur_node = self.dummy
        
        self.helper(root)
        
        self.cur_node.right = self.dummy.right
        self.dummy.right.left = self.cur_node
        
        return self.dummy.right
    
    
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        
        self.cur_node.right = Node(root.val)
        self.cur_node.right.left = self.cur_node
        self.cur_node = self.cur_node.right
        
        self.helper(root.right)
        

    
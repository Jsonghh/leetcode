"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        # use a function record path A and B from the root node 
        
        path_a = self.get_path(root, A)
        path_b = self.get_path(root, B)
        
        
        # if len(path_a) > len(path_b):
        #     self.lowestCommonAncestorII(root, B, A)
            
        for a_node in path_a:
            for b_node in path_b:
                if a_node.val == b_node.val:
                    return a_node
                    
                    
    def get_path(self, root, node):
        path = []
        while node:
            path.append(node)
            node = node.parent
        return path
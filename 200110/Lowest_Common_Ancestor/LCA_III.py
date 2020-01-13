
class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        self.parent = None
        self.helper(root, A, B)
        return self.parent

        # return (A_in_root, B_in_root)
    def helper(self, root, A, B):
        if not root:
            return False, False
        A_inleft, B_inleft = self.helper(root.left, A, B)
        A_inright, B_inright= self.helper(root.right, A, B)
        
        A_inroot = A_inleft or root == A or A_inright
        B_inroot = B_inleft or root == B or B_inright
        
        #if already found parent, then dont assign again
        if not self.parent and A_inroot and B_inroot:
            self.parent = root 
        return A_inroot, B_inroot
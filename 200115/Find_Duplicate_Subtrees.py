#_Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def __init__(self,):
        self.count = defaultdict(int)
        self.ans = []
        
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        serial_root = self.get_serial(root)
        return self.ans
    
    def get_serial(self, node):
        if not node:
            return '#'
        serial = str(node.val) + self.get_serial(node.left) + self.get_serial(node.right)
        self.count[serial] += 1
        if self.count[serial] == 2:
            self.ans.append(node)
        return serial
    
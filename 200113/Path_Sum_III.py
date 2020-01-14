# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self,):
        self.cnt = 0
        self.calculated_sums = {}
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        self.helper(root, 0, sum)
        return self.cnt
        
    def helper(self, node, cur_sum, target_sum):
        if not node:
            return
        cur_sum += node.val
        if cur_sum == target_sum:
            self.cnt += 1
            
        before_sum = cur_sum - target_sum
        if before_sum in self.calculated_sums:
            self.cnt += self.calculated_sums[before_sum] 
            
        for nnode in [node.left, node.right]:
            self.calculated_sums[cur_sum] = self.calculated_sums.get(cur_sum, 0) + 1
            self.helper(nnode, cur_sum, target_sum)
            self.calculated_sums[cur_sum] -= 1
            
        return
        
        
        
        
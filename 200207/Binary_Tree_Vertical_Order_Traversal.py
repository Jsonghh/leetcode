# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue= [(root, 0)]
        nums = defaultdict(list)
        
        while queue:
            node, x = queue.pop(0)
            if node.left:
                queue.append((node.left, x - 1))
            if node.right:
                queue.append((node.right, x + 1))
            nums[x].append(node.val)
            
        ans = [ nums[num]  for num in sorted(nums.keys())]
        
        return ans
                
            
            
        
        
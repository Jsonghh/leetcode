# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
#         O(klogk) + O(N)
        self.min_diffs = []
        self.helper(root, target, k)
        ans = []
        for diff, node_val in self.min_diffs:
            ans.append(node_val)
        return ans
    
    
    def helper(self, node, target, k):
        if not node:
            return
        
        if node.val <= target and node.right:
            self.helper(node.right, target, k)

        if node.val >= target and node.left:
            self.helper(node.left, target, k)
        
        diff = abs(node.val - target)
        if len(self.min_diffs) < k or -diff > self.min_diffs[0][0]:
            heapq.heappush(self.min_diffs, (-diff, node.val))
            if len(self.min_diffs) > k:
                heapq.heappop(self.min_diffs)
            
            if node.val < target and node.left:
                self.helper(node.left, target, k)
            if node.val > target and node.right: 
                self.helper(node.right, target, k)
        
        return 



# CONVERT TREE TO A LIST

#         inorder = self.get_inorder(root)
#         left = 0
#         for i in range(1, len(inorder)):
#             if inorder[i] >= target:
#                 left = i - 1
#                 break
#         right = left + 1

#         ans = []
#         while len(ans) < k:
#             if self.take_left(inorder, left, right, target):
#                 ans.append(inorder[left])
#                 left -= 1
#             else:
#                 ans.append(inorder[right])
#                 right += 1
#         return ans
    
#     def take_left(self, inorder, left, right, target):
#         if left < 0:
#             return False
#         if right >= len(inorder):
#             return True
#         return target - inorder[left] < inorder[right] - target
    
#     def get_inorder(self, root):
#         if not root:
#             return []
#         inorder, stack = [], []
#         while root:
#             stack.append(root)
#             root = root.left
            
#         while stack:
#             node = stack.pop()
#             inorder.append(node.val)
#             if node.right:
#                 root = node.right
#                 while root:
#                     stack.append(root)
#                     root = root.left
#         return inorder
            
                
                

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)
        
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        root = TreeNode(mid.val)
        slow.next = None
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root
        
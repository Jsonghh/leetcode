# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = 0, 0
        while l1:
            n1 = n1 * 10 + l1.val
            l1 = l1.next
            
        while l2:
            n2 = n2 * 10 + l2.val
            l2 = l2.next
            
        dummy = ListNode(-1)
        cur = dummy
        for char in str(n1 + n2):
            cur.next = ListNode(int(char))
            cur = cur.next
            
        return dummy.next
            
            
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7        
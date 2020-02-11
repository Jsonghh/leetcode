# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        ehead = head.next
        odd, even = head, ehead
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next= even.next.next
            even = even.next
            
        odd.next = ehead
        
        return head
            
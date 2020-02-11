# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        
        while cur and cur.next:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
                
            cur = cur.next
            
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev = ListNode(-1)
        dummy = prev
        prev.next = head
        while prev.next and prev.next.next:
            cur = prev.next
            
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = cur
            prev.next = tmp
            
            prev = cur
            
        return dummy.next
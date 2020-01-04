# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        cnt_node = head
        pre, cur = dummy, head
        length = 0
        while cnt_node:
            length += 1
            cnt_node = cnt_node.next
        if length < n:
            return None
        cnt = 0
        while cnt < length - n:
            pre = cur
            cur = cur.next
            cnt += 1
        pre.next = cur.next
        return dummy.next
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def helper(self, prev, end):
        cur = prev.next
        while prev.next != end:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
        return cur


    def reverseKGroup(self, l, k):
        if not l:
            return l
        prev = ListNode(-1)
        prev.next, end = l, l
        new_head = prev
        cnt = 0
        while end:
            cnt += 1
            if k == cnt:
                prev = self.helper(prev, end)
                end = prev.next
                cnt = 0
            else:
                end = end.next
        return new_head.next





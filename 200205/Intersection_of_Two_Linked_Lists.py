# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = set()
        pa, pb = headA, headB
        while pa:
            visited.add(pa)
            pa = pa.next
            
        while pb:
            if pb in visited:
                return pb
            
            pb = pb.next



            
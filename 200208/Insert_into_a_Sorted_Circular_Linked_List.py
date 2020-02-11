"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        
        prev, curr = head, head.next
        to_insert = False
        
        while True:

            if prev.val <= insertVal <= curr.val:
                to_insert = True
                
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    to_insert = True

            if to_insert:
                prev.next = Node(insertVal, curr)
                return head

            prev, curr = curr, curr.next
            if prev == head:
                break
            
        prev.next = Node(insertVal, curr)
        return head
            
        
        
        

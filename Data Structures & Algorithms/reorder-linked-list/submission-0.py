# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        Q = deque()
        while head is not None:
            Q.append(head)
            head = head.next


        head = curr = Q.popleft()
        while len(Q) > 0:
            curr.next = Q.pop()
            curr = curr.next

            if len(Q) > 0:
                curr.next = Q.popleft()
                curr = curr.next
        
        curr.next = None
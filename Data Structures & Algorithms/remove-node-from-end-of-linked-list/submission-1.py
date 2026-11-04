# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        curr, stack = head, []
        while curr is not None:
            stack.append(curr)
            curr = curr.next
        
        curr = None

        for _ in range(n):
            curr = stack.pop()
        
        prev = stack.pop() if len(stack) > 0 else None

        if prev is None:
            # Case: remove head node
            return curr.next if curr is not None else None
        
        # Case: remove middle or last node
        prev.next = curr.next
        return head
import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
k + n log(k)
    k <-- number of lists
    n <-- total number of nodes
"""

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        
        heap = []
        
        for i in range(len(lists)):
            node = lists[i]
            if node: 
                heapq.heappush(heap, (node.val, i))

        head = curr = ListNode(0, None) # dummy node

        while len(heap) > 0:
            min_node_i = heapq.heappop(heap)[1]
            min_node = lists[min_node_i]

            
            if min_node.next: 
                lists[min_node_i] = min_node.next
                heapq.heappush(heap, (min_node.next.val, min_node_i))

            curr.next = min_node
            curr = curr.next
            curr.next = None




        return head.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # start with first element of lst
        for lst_idx, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, lst_idx, node))

        
        dummy = ListNode()
        curr = dummy

        while min_heap:
            node_val, lst_idx, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, lst_idx, node.next))
        
        return dummy.next


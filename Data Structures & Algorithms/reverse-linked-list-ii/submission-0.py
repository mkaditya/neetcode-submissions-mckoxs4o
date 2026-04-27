# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left_prev, curr = dummy, head

        for _ in range(left-1): # hop is 1 less than index
            left_prev, curr = curr, curr.next
        
        prev = None
        for _ in range(right - left + 1):
            prev, curr.next, curr = curr, prev, curr.next
        
        left_prev.next.next = curr
        left_prev.next = prev
        return dummy.next
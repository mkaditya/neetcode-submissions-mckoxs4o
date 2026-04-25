# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head  # tortoise, hear

        while fast and fast.next: # if there is loop it doesn't terminate
            fast = fast.next.next
            slow = slow.next 
            if slow == fast: # they met due to cycle.
                return True
        return False

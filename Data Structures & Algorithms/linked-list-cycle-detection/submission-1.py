# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        first, second = head, head.next
        while first and second:
            if first == second:
                return True
            first = first.next
            second = second.next.next if second and second.next else None

        return False

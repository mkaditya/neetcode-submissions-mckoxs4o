# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        prev, curr = None, slow

        while curr:
            prev, curr.next, curr = curr, prev, curr.next
        
        first, second = head, prev

        while second.next:
            first_next, second_next = first.next, second.next
            first.next, second.next = second, first_next
            first, second = first_next, second_next


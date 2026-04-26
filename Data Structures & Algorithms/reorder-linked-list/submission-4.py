# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 1, 2, 3, 4, 5, 6, 7, 
        # find mid with slow
        slow, fast = head, head  # 1, 1

        while fast and fast.next: 
            slow, fast = slow.next, fast.next.next # 4, 7
        
        prev, curr = None, slow

        # reverse second half
        while curr:
            prev, curr.next, curr = curr, prev, curr.next
        
        first, second = head, prev

        # merge two lists
        while second and second.next:
            first_next, second_next = first.next, second.next
            first.next, second.next = second, first_next
            first, second = first_next, second_next


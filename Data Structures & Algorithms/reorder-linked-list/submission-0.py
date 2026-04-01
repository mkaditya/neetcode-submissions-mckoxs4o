# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        reverse_head = prev

        left, right = head, reverse_head

        while right and left:
            left_next = left.next
            right_next =right.next
            left.next = right
            right.next = left_next

            left = left_next
            right = right_next

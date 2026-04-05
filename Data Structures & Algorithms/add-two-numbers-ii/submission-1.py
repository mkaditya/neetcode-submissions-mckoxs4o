# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = self.reverse(l1), self.reverse(l2)

        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2 or carry:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
        
            carry = sum_val // 10
            curr.next = ListNode(sum_val % 10)
            curr = curr.next
        return self.reverse(dummy.next)

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next, curr.next = curr.next, prev
            prev, curr = curr, next
        return prev
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_list, second_list, dummy_head = l1, l2, ListNode()
        tail = dummy_head
        carry = 0

        while first_list or second_list or carry:
            val1 = first_list.val if first_list else 0
            val2 = second_list.val if second_list else 0

            curr_sum = val1 + val2 + carry
            carry = curr_sum // 10

            tail.next = ListNode(curr_sum % 10)
            tail = tail.next

            if first_list:
                first_list = first_list.next
            
            if second_list:
                second_list = second_list.next

        return dummy_head.next
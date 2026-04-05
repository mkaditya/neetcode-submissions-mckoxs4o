# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = self.list_to_stack(l1), self.list_to_stack(l2)

        carry, head = 0 , None

        while s1 or s2 or carry:
            v1 = s1.pop() if s1 else 0
            v2 = s2.pop() if s2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            
            node = ListNode(total % 10)
            node.next = head
            head = node
        
        return head


    def list_to_stack(self, lst):
        stack = []
        while lst:
            stack.append(lst.val)
            lst = lst.next
        return stack

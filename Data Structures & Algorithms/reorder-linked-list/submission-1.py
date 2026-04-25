# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #  0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        #  0 -> 1 -> 2 -> 3 ,7 -> 6 -> 5 -> 4
        # 0 -> 7 -> 1 -> 6 -> 2 -> 5 -> 3 -> 4
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid_point = slow
        list2, mid_point.next = mid_point.next, None # breaks into two lists

        # reverse list2
        curr, prev = list2, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        list2 = prev
        
        # merge
        dummy = curr = ListNode()
        list1 = head
        is_list1 = True
        while list1 and list2:
            if is_list1:
                curr.next, list1, curr = list1, list1.next, list1
                is_list1 = False
            else:
                curr.next, curr, list2 = list2, list2, list2.next
                is_list1 = True
        curr.next = list1 if list1 else list2
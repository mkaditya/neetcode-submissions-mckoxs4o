"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # o1 -> o2 -> o3 , o1 -> o3, o2 -> o1
        # h1 -> h2 -> h3 , h1 -> h3, h2 -> h1
        # o1 -> h1 -> o2 -> h2 -> o3 -> h3, 

        curr = head
        while curr:
            dup = Node(curr.val, curr.next, None)
            curr.next = dup
            curr = dup.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr, copy_head = head, head.next if head else None
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        return copy_head

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
        if not head:
            return None

        self._weave_normal(head)
        self._weave_random(head)
        return self._unweave(head)

    def _weave_normal(self, head):
        # A->A'->B->B'->C->C'

        curr = head
        while curr:
            duplicate = Node(curr.val)
            duplicate.next = curr.next
            curr.next = duplicate
            curr = duplicate.next

    def _weave_random(self, head):
        # A->A'->B->B'->C->C' (assume A->C in random)
        curr = head
        while curr:
            duplicate = curr.next
            if curr.random:
                duplicate.random = curr.random.next # you need to map to duplicate of random
            curr = duplicate.next
    
    def _unweave(self, head):
        # A->A'->B->B'->C->C'
        clone_head = head.next
        curr = head
        while curr:
            duplicate = curr.next
            curr.next = duplicate.next
            if duplicate.next:
                duplicate.next = duplicate.next.next
            curr = curr.next
        return clone_head
        
        
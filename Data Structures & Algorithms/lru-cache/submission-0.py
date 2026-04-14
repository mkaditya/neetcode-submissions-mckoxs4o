class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.dummy_head = Node(0, 0) # dummy head
        self.dummy_tail = Node(0, 0)
        self.dummy_head.next, self.dummy_tail.prev = self.dummy_tail, self.dummy_head
    
    def _insert(self, key, val):
        node = Node(key, val)
        # insert as head
        dummy_head, head = self.dummy_head, self.dummy_head.next
        self.dummy_head.next, head.prev = node, node
        node.next, node.prev = head, dummy_head
        self.cache[key] = node

    def _remove(self, key):
        if key not in self.cache:
            return
        node = self.cache[key]
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        del self.cache[key]   
        

    def get(self, key: int) -> int:
        return_val = -1
        if key in self.cache:
            return_val = self.cache[key].val
            self._remove(key)
            self._insert(key, return_val)
        return return_val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(key)
        
        self._insert(key, value)

        if len(self.cache) > self.capacity:
            del_node = self.dummy_tail.prev
            self._remove(del_node.key)
        

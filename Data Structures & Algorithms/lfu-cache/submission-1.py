class FreqNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.freq = 1
        self.prev, self.next = None, None

class DLL:
    def __init__(self):
        self.head, self.tail = FreqNode(0, 0), FreqNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def add(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
    
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def pop(self):
        if self.tail.prev == self.head:
            return None # noting to pop
        node = self.tail.prev
        self.remove(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_freq_node = {}
        self.freq_to_dll = {}
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_freq_node:
            return -1
        
        node = self.key_to_freq_node[key]
        self._update(node)
        return node.val

    def _update(self, node):
        freq = node.freq
        dll = self.freq_to_dll[freq]
        dll.remove(node)

        if freq == self.min_freq and dll.head.next == dll.tail:
            self.min_freq += 1
        
        node.freq += 1
        self.freq_to_dll.setdefault(node.freq, DLL()).add(node)

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_freq_node:
            node = self.key_to_freq_node[key]
            node.val = value
            self._update(node)
        else:
            if len(self.key_to_freq_node) == self.capacity:
                dll = self.freq_to_dll[self.min_freq]
                removed_node = dll.pop()
                del self.key_to_freq_node[removed_node.key]

            new_node = FreqNode(key, value)
            self.key_to_freq_node[key] = new_node
            self.freq_to_dll.setdefault(1, DLL()).add(new_node)
            self.min_freq = 1

class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

# TODO Aditya revise it again
class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def hash(self, key: int) -> int:
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        keys_list = self.map[self.hash(key)]
        while keys_list.next:
            if keys_list.next.key == key:
                keys_list.next.val = value
                return
            keys_list = keys_list.next
        keys_list.next = ListNode(key, value)


    def get(self, key: int) -> int:
        keys_list = self.map[self.hash(key)]
        while keys_list.next:
            if keys_list.next.key == key:
                return keys_list.next.val
            keys_list = keys_list.next
        return -1
        

    def remove(self, key: int) -> None:
        keys_list = self.map[self.hash(key)]
        while keys_list.next:
            if keys_list.next.key == key:
                keys_list.next = keys_list.next.next
                return
            keys_list = keys_list.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
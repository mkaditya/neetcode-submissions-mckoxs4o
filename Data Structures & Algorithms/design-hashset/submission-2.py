class MyHashSet:

    def __init__(self):
        self.bins = int(1000000/32 + 1) # dividing one million into n buckets of 32 size. 32 is integer size
        self.set = [0] * (self.bins)

    def add(self, key: int) -> None:
        self.set[key // 32] = self.set[key // 32] | (1 << key % 32)

    def remove(self, key: int) -> None:
        self.set[key // 32] = self.set[key // 32] & ~(1 << key % 32)

    def contains(self, key: int) -> bool:
        return (self.set[key // 32] & 1 << key % 32) != 0


        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
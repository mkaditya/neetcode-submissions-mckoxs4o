class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.is_unique = {}
        for num in nums:
            self.add(num)

    def add(self, num: int) -> None:
        if num not in self.is_unique:
            self.is_unique[num] = True
            self.q.append(num)
        else:
            self.is_unique[num] = False

    def showFirstUnique(self) -> int:
        while self.q and not self.is_unique[self.q[0]]:
            self.q.popleft()
        if self.q:
            return self.q[0]
        return -1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

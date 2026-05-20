class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = OrderedDict()
        self.is_duplicated = {}
        for num in nums:
            self.add(num)

    def add(self, value: int) -> None:
        if value in self.is_duplicated:
            if not self.is_duplicated[value]:
                self.q.pop(value)
                self.is_duplicated[value] = True
        else:
            self.q[value] = None
            self.is_duplicated[value] = False

    def showFirstUnique(self) -> int:
        return next(iter(self.q), -1)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

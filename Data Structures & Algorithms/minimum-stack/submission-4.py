class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        existing_min = self.getMin()
        min_val = min(val, existing_min if existing_min is not None else float("inf") )
        self.stack.append([val, min_val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        

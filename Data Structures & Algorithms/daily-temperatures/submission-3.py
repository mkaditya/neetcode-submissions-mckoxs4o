class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []

        for idx in range(0, len(temps)):
            # pop all cooler dates if they exist.
            while stack and temps[stack[-1]] < temps[idx]:
                prev_idx = stack.pop()
                res[prev_idx] = idx - prev_idx
            stack.append(idx)
        return res

class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []

        for idx in range(0, len(temps)):
            while stack and temps[stack[-1]] < temps[idx]:
                temp_idx = stack.pop()
                res[temp_idx] = idx - temp_idx
            stack.append(idx)

        return res
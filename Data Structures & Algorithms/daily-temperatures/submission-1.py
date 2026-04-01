class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []

        for idx, temp in enumerate(temps):
            while stack and temp > stack[-1][0]:
                nTemp, nIdx = stack.pop()
                res[nIdx] = idx - nIdx
            stack.append((temp, idx))
        return res
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []

        for curr_idx, curr_temp in enumerate(temps):
            while stack and curr_temp > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = curr_idx - prev_idx # difference betweend idx of next big eleemnt
            stack.append((curr_temp, curr_idx))
        return res
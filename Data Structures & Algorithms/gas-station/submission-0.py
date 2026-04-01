class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = tank = start = 0

        for idx in range(len(gas)):
            diff = gas[idx] - cost[idx]
            total += diff
            tank += diff
            if tank < 0:
                start = idx + 1
                tank = 0
        return start if total >= 0 else -1

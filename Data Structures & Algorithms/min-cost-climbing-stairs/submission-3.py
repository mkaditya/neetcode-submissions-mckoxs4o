class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost(n) = min(cost(n-1), cost(n-2))
        n = len(cost)

        cost_to_reach = [None] * (n+1)
        cost_to_reach[0] = 0
        cost_to_reach[1] = 0

        for i in range(2, n+1):
            cost_to_reach[i] = min(cost_to_reach[i-1] + cost[i-1],
                                   cost_to_reach[i-2] + cost[i-2])

        return cost_to_reach[n]


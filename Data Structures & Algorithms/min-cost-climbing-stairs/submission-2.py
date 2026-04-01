class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost(n) = min(cost(n-1), cost(n-2))
        n = len(cost)
        if n <= 2: 
            return min(cost)
        
        cost_n = [None] * (n+1)
        cost_n[0] = 0
        cost_n[1] = 0
        cost_n[2] = min(cost[0], cost[1])

        for i in range(3, n+1):
            cost_n[i] = min(cost_n[i-1] + cost[i-1], cost_n[i-2] + cost[i-2])

        return cost_n[n]


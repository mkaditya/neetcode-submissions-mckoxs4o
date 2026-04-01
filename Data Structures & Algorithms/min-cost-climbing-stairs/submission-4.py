class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_idx_minus_2, cost_idx_minus_1 = 0, 0

        for idx in range(len(cost)):
            cost_idx_minus_2, cost_idx_minus_1 = cost_idx_minus_1 , min(cost_idx_minus_2 + cost[idx], cost_idx_minus_1 + cost[idx])

        return min(cost_idx_minus_1, cost_idx_minus_2)
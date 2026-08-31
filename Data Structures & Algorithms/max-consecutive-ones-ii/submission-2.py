class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best, start_idx, budget = 0, 0, 1

        for idx, num in enumerate(nums):
            if num == 0:
                budget -= 1
            if budget < 0:
                if nums[start_idx] == 0:
                    budget += 1
                start_idx += 1
            best = max(best, idx - start_idx + 1)
        return best
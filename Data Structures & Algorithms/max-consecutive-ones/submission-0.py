class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        curr_iter = 0

        for num in nums:
            if num:
                curr_iter += 1
            else:
                result = max(result, curr_iter)
                curr_iter = 0
        return max(result, curr_iter)
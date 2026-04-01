class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[idx % n] for idx in range(2 * n)]
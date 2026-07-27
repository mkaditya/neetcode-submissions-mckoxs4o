class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [nums[idx % len(nums)] for idx in range(2 * len(nums))]
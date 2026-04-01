class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for idx in range(n*2):
            ans.append(nums[idx % n])
        return ans
        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        return any(num in seen or seen.add(num) for num in nums)
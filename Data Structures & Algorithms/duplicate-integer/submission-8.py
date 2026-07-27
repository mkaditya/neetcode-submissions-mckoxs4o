class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_check = set()
        return any(num in dup_check or dup_check.add(num) for num in nums)
        
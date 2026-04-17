class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_checker = set()
        for num in nums:
            if num in dup_checker:
                return True
            dup_checker.add(num)
        return False
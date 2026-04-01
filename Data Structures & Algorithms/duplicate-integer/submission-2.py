class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        return False
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in seen:
                return [seen[diff], idx]
            seen[nums[idx]] = idx

        return []
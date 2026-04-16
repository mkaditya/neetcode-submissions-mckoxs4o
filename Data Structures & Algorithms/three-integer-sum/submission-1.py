# TODO: Aditya do again
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for first_idx in range(n):
            if first_idx > 0 and nums[first_idx] == nums[first_idx - 1]:
                continue

            target = 0 - nums[first_idx]
            l, r = first_idx + 1, n - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum == target:
                    result.append([nums[first_idx], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return result

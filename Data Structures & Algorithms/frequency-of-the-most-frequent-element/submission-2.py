class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_freq, curr_window = 0, 0
        l, r = 0, 0
        while r < len(nums):
            curr_window += nums[r]
            # amount of budget required to make everything nums[r] in the window (if not valid, shrink window)
            while (r - l + 1) * nums[r] > curr_window + k:
                curr_window -= nums[l]
                l += 1
            max_freq = max(max_freq, r - l + 1)
            r += 1
        return max_freq
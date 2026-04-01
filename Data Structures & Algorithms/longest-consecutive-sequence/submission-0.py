class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            leftVal = num -  1
            if leftVal in numSet:
                continue # can't be the beginning of seq
            length = 1
            while num + 1 in numSet:
                length += 1
                num = num + 1
            longest = max(longest, length)
        return longest
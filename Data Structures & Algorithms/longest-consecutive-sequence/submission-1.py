class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq_length = min(1, len(nums))

        for num in nums:
            if num - 1 in nums_set:
                continue # smallest number will look all the way up to get seq
            
            length = 1
            while num + length in nums_set:
                length += 1
            longest_seq_length = max(longest_seq_length, length)
        return longest_seq_length
            
            
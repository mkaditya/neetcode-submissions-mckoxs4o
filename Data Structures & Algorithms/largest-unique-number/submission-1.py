class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        return max([key for key, val in freq_map.items() if val == 1], default=-1)
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        uniq_nums = [key for key, val in freq_map.items() if val == 1]
        if not uniq_nums:
            return -1
        return max(uniq_nums)
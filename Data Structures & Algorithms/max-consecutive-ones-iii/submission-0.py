class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start_idx, zero_count = 0, 0
        best = 0

        for idx, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            while zero_count > k:
                if nums[start_idx] == 0:
                    zero_count -= 1
                start_idx += 1
            best = max(best, idx - start_idx + 1)
        return best
            
                

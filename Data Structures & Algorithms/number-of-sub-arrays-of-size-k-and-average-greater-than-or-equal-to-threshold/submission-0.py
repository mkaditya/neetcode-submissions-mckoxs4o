class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum, curr_sum = threshold * k, 0
        result = 0
        for idx in range(k):
            curr_sum += arr[idx]
        
        if curr_sum >= target_sum:
            result += 1

        for idx in range(k, len(arr)):
            leaving_val, curr_val = arr[idx - k], arr[idx]
            curr_sum -= leaving_val
            curr_sum += curr_val
            if curr_sum >= target_sum:
                result += 1
        return result
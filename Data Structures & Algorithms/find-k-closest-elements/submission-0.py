class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left_idx, right_idx = 0, len(arr) - 1
        res = []

        while right_idx - left_idx >= k: 
            left_diff = abs(arr[left_idx] - x)
            right_diff = abs(arr[right_idx] - x)

            if left_diff > right_diff:
                left_idx += 1
            else:
                right_idx -= 1
        return arr[left_idx: right_idx + 1]
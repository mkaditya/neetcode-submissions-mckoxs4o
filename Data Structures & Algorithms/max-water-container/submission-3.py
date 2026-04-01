class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_idx, right_idx = 0, len(heights) - 1
        max_area = 0

        while left_idx < right_idx:
            area = min(heights[left_idx], heights[right_idx]) * (right_idx - left_idx)
            max_area = max(max_area, area)
            if heights[left_idx] < heights[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1
        return max_area
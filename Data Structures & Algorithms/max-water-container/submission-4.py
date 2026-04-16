class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_idx, r_idx = 0, len(heights) - 1
        max_area = 0

        while l_idx <= r_idx:
            width = r_idx - l_idx
            height = min(heights[l_idx], heights[r_idx])
            max_area = max(max_area, width * height)
            if heights[l_idx] < heights[r_idx]:
                l_idx += 1
            else:
                r_idx -= 1
        
        return max_area
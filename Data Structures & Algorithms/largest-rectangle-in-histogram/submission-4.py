class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for idx, height in enumerate(heights + [0]):
            start_idx = idx
            while stack and stack[-1][1] > height:
                popped_idx, popped_height = stack.pop()
                max_area = max(max_area, (idx - popped_idx) * popped_height)
                start_idx = popped_idx
            stack.append((start_idx, height))
        
        return max_area
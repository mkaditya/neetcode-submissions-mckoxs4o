class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for idx, height in enumerate(heights + [0]):
            start_idx = idx
            while stack and stack[-1][1] > height:
                popped_idx, popped_height = stack.pop()
                max_area = max(max_area, (idx - popped_idx) * popped_height)
                # You can start from this earlier index because all bars between popped_idx and your current index are at least as tall as you.
                start_idx = popped_idx
            stack.append((start_idx, height))
        
        return max_area
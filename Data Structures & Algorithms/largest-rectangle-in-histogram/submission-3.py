class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for idx, height in enumerate(heights):
            batchIdx = idx
            while stack and stack[-1][1] >= height:
                cIdx, cHeight = stack.pop()
                maxArea = max((idx - cIdx) * cHeight, maxArea)
                batchIdx = cIdx
            stack.append((batchIdx, height))

        while stack:
            cIdx, cHeight = stack.pop()
            maxArea = max((len(heights) - cIdx) * cHeight, maxArea) 
        return maxArea
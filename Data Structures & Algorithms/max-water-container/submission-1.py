class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftIdx = 0
        rightIdx = len(heights) - 1
        max_area = 0

        while leftIdx < rightIdx:
            width = rightIdx - leftIdx
            height = min(heights[leftIdx], heights[rightIdx])
            max_area = max(max_area, width * height)
            if heights[leftIdx] < heights[rightIdx]:
                leftIdx += 1
            else:
                rightIdx -= 1
        return max_area

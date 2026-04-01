class Solution {
    public int maxArea(int[] heights) {
        int result = 0;

        int leftIdx = 0;
        int rightIdx = heights.length - 1;

        while (leftIdx < rightIdx) {
            int area = (rightIdx - leftIdx) * Math.min(heights[leftIdx], heights[rightIdx]);
            result = Math.max(area, result);

            if (heights[leftIdx] < heights[rightIdx]) {
                leftIdx++;
            } else {
                rightIdx--;
            }
        }

        return result;
    }
}

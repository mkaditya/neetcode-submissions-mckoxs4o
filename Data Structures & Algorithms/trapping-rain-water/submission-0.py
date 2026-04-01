class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l,r = 0, len(height) - 1

        maxLeft,maxRight = height[l], height[r]
        res = 0

        # Always move the side with the smaller max height, because the trapped water is limited by the shorter boundary.
        # Move the smaller side, update its max, and add trapped water.
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max (maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max (maxRight, height[r])
                res += maxRight - height[r]
        return res

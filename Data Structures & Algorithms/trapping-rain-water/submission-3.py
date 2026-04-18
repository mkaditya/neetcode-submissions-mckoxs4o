# TODO: Aditya do again
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return -1
        left_max = height[0]
        right_max = height[-1]
        

        l, r = 0, len(height) -1
        water = 0

        while l <= r:
            left_height = height[l]
            right_height = height[r]
            if left_max < right_max:
                left_max = max(left_max, left_height)
                water += left_max - left_height
                l += 1
            else:
                right_max = max(right_max, right_height)
                water += right_max - right_height
                r -= 1
        
        return water

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, large = nums1, nums2
        if len(nums1) > len(nums2):
            small, large = nums2, nums1

        total_len = len(small) + len(large)
        half_len = total_len // 2

        left, right = 0, len(small)

        while left <= right:
            i = (left + right) // 2
            j = half_len - i # if we take i elements from small array, we take half -i from large array

            small_arr_left_max = small[i - 1] if i > 0 else float("-inf") # max element in left partition
            small_arr_right_min = small[i] if i < len(small) else float("inf") # min element in right partition

            large_arr_left_max = large[j - 1] if j > 0 else float("-inf") # max element in left partition
            large_arr_right_min = large[j] if j < len(large) else float("inf") # min element in right partition

            if small_arr_left_max <= large_arr_right_min and large_arr_left_max <= small_arr_right_min: # array is divided properly
                if total_len % 2 != 0: # odd number of elements
                    return float(min(small_arr_right_min, large_arr_right_min))
                return (max(small_arr_left_max, large_arr_left_max) + min(small_arr_right_min, large_arr_right_min)) / 2.0
            
            if small_arr_left_max > large_arr_right_min:
                right = i - 1
            else:
                left = i + 1
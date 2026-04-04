class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        n = mountainArr.length()

        # Find the peak index using binary search
        # The peak is where the array transitions from increasing to decreasing
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi)//2
            # Compare mid with mid+1 to determine if we're on the ascending or descending side
            if mountainArr.get(mid) < mountainArr.get(mid + 1):  # Still ascending, peak is to the right
                lo = mid + 1
            else:  # Descending or at peak, peak is at mid or to the left
                hi = mid
        peak = lo  # Peak index found

        # Search in the left (ascending) portion of the mountain
        lo, hi = 0, peak
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:  # Target is larger, search right
                lo = mid + 1
            else:  # Target is smaller, search left
                hi = mid - 1
        
        # If not found in left portion, search in the right (descending) portion
        lo, hi = peak + 1, n - 1
        while lo <= hi:
            mid = (lo + hi)//2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:  # On descending side, larger values are to the left
                lo = mid + 1
            else:  # Smaller values are to the right
                hi = mid - 1
        
        return -1  # Target not found in either portion
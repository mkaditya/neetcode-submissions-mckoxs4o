# TODO: Do this again.
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        peak = self.find_peak(mountainArr)
        
        # Check left side
        result = self.binary_search(mountainArr, target, 0, peak, True)
        if result != -1: return result
        
        # Check right side
        return self.binary_search(mountainArr, target, peak, n - 1, False)
    
    def find_peak(self, arr):
        lo, hi = 0, arr.length() - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr.get(mid) < arr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    def binary_search(self, arr, target, lo, hi, ascending):
        while lo <= hi:
            mid = (lo + hi) // 2
            val = arr.get(mid)
            
            if val == target: return mid
            
            if (ascending and val < target) or (not ascending and val > target):
                lo = mid + 1  # Move right
            else:
                hi = mid - 1  # Move left
        
        return -1
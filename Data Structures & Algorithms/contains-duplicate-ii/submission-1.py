class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) <= 1:
            return False
        l, r = 0, 1
        seen = set()
        seen.add(nums[l])

        while r < len(nums):
            if nums[r] in seen:
                return True
            
            seen.add(nums[r])
            r = r + 1
            if r - l > k:
                seen.remove(nums[l])
                l = l + 1
        
        return False
            
            
            

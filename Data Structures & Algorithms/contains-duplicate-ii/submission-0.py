class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums and len(nums) <= 1:
            return False

        window = set()
        l, r = 0, 1
        window.add(nums[l])

        while r < len(nums):
            if r - l > k:
                window.remove(nums[l])
                l = l + 1
            if nums[r] in window:
                return True
            window.add(nums[r])
            r = r + 1
        return False
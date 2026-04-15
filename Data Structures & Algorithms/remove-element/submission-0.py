class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx, n = 0, len(nums)
        while idx < n:
            if nums[idx] == val:
                n = n -1
                nums[idx] = nums[n]
            else:
                idx += 1
        return n
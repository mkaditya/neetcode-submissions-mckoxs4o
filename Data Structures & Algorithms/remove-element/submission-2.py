class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx, l = 0, len(nums)
        
        while idx < l:
            if nums[idx] == val:
                nums[idx] = nums[l-1]
                l = l - 1
            else:
                idx += 1
        return l
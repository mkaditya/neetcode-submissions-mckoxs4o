import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums
    
    def quick_sort(self, nums: List[int], left:int, right:int) -> None:
        if right <= left + 1:
            if right == left + 1 and nums[right] < nums[left]:
                nums[left], nums[right] = nums[right], nums[left]
            return
        
        pivot = self.partition(nums, left, right)
        self.quick_sort(nums, left, pivot - 1)
        self.quick_sort(nums, pivot + 1, right)
    
    def partition(self, nums: List[int], left, right) -> int:
        pivot_idx = random.randint(left, right)
        nums[pivot_idx], nums[right]  = nums[right], nums[pivot_idx]
        smaller_idx, pivot = left, nums[right]

        for idx in range(left, right):
            if nums[idx] <= pivot:
                nums[smaller_idx], nums[idx] = nums[idx], nums[smaller_idx]
                smaller_idx += 1

        nums[smaller_idx], nums[right] = nums[right], nums[smaller_idx]
        return smaller_idx
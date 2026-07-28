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
        mid = (left + right) // 2
        nums[mid], nums[left+1] = nums[left+1], nums[mid]

        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left + 1] > nums[right]:
            nums[left+1], nums[right] = nums[right], nums[left+1]
        if nums[left] > nums[left+1]:
            nums[left], nums[left+1] = nums[left+1], nums[left]
        
        pivot = nums[left+1]
        i = left + 1
        j = right

        while True:
            while True:
                i += 1
                if not nums[i] < pivot:
                    break
            while True:
                j -= 1
                if not nums[j] > pivot:
                    break
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[left+1], nums[j] = nums[j], nums[left+1]
        return j
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue # we did this math previously.
            
            leftIdx, rightIdx = idx+1, len(nums) - 1
            while leftIdx < rightIdx:
                threeSum = nums[idx] + nums[leftIdx] + nums[rightIdx]
                if threeSum == 0:
                    res.append([nums[idx], nums[leftIdx], nums[rightIdx]])
                    # avoid duplicates which can happen due to duplicate values from leftIdx & rightIdx iterations
                    while leftIdx < rightIdx and nums[leftIdx] == nums[leftIdx + 1]:
                        leftIdx += 1
                    while leftIdx < rightIdx and nums[rightIdx] == nums[rightIdx - 1]:
                        rightIdx -= 1
                    leftIdx += 1
                    rightIdx -= 1
                elif threeSum < 0:
                    leftIdx += 1
                else:
                    rightIdx -= 1
        return res
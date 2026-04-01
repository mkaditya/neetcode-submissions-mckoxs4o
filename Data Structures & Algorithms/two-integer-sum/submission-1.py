class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        left, right = 0, len(nums)-1
        while left < right:
            curr_sum = A[left][0] + A[right][0]
            if target == curr_sum:
                return [
                    min(A[left][1], A[right][1]), 
                    max(A[left][1], A[right][1])
                ]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        return []
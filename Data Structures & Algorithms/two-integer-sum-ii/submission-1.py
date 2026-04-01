class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIdx = 0
        rightIdx = len(numbers) - 1

        while leftIdx < rightIdx:
            sum = numbers[leftIdx] + numbers[rightIdx]
            if sum == target:
                return [leftIdx + 1, rightIdx + 1]
            elif sum < target:
                leftIdx += 1
            else:
                rightIdx -= 1
        return []
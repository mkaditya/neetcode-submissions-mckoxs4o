class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIdx, rightIdx = 0, len(numbers) - 1

        while leftIdx < rightIdx:
            current_sum = numbers[leftIdx] + numbers[rightIdx]
            if current_sum == target:
                return [leftIdx + 1, rightIdx + 1]
            elif current_sum < target:
                leftIdx += 1
            else:
                rightIdx -= 1
        return []
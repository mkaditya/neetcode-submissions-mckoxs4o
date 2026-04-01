class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_idx, right_idx = 0, len(numbers) - 1

        while left_idx < right_idx:
            curr_sum = numbers[left_idx] + numbers[right_idx]
            if curr_sum == target:
                return [left_idx + 1, right_idx + 1]
            elif curr_sum < target:
                left_idx += 1
            else:
                right_idx -= 1
        return []
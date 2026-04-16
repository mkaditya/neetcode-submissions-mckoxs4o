class Solution:
    # sub-optimal just for furn
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx in range(len(numbers)):
            left_idx = idx + 1
            right_idx = len(numbers) - 1
            sub_target = target - numbers[idx]

            while left_idx <= right_idx:
                mid = (left_idx + right_idx) // 2
                if numbers[mid] == sub_target:
                    return [idx+1, mid+1]
                elif numbers[mid] < sub_target:
                    left_idx = mid + 1
                else:
                    right_idx = mid - 1
               
        return []
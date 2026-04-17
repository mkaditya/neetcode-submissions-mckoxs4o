
# TODO: Math Algo --> Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, element = 0, 0

        for num in nums:
            if count == 0:
                element = num
            
            if num == element:
                count += 1
            else:
                count -= 1
        
        return element
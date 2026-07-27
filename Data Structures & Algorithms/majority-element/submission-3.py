
# TODO: Math Algo --> Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, winner = 0, 0
        for num in nums:
            if count == 0:
                count, winner = 1, num
            else:
                if num == winner:
                    count += 1
                else:
                    count -= 1
        return winner
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in reversed(range(len(digits))):
            # do +1 for each element in digits, if it doesn't result in carry return
            if digits[i] < 9:
                digits[i] +=1
                return digits
            digits[i] = 0
        return [1] + digits
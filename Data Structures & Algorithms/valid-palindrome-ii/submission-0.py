class Solution:
    def validPalindrome(self, s: str, budget = 1) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif budget == 1:
                return self.validPalindrome(s[l+1:r+1], 0) or self.validPalindrome(s[l:r], 0)
            else:
                return False # no budget
        return True
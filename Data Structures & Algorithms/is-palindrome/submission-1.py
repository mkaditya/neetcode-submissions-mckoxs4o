class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_idx, right_idx = 0, len(s) - 1
        while left_idx < right_idx:
            while left_idx < right_idx and not s[left_idx].isalnum():
                left_idx = left_idx + 1
            while left_idx < right_idx and not s[right_idx].isalnum():
                right_idx = right_idx - 1
            if left_idx < right_idx and s[left_idx].lower() != s[right_idx].lower():
                return False
            left_idx = left_idx + 1
            right_idx = right_idx - 1
        return True
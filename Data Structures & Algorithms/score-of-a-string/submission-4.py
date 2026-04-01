class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(
            abs(ord(s[idx]) - ord(s[idx+1])) for idx in range(len(s) - 1)
        )
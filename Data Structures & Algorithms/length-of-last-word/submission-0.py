class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx, len_of_last = len(s) - 1, 0

        while idx >= 0 and s[idx] == " ":
            idx -= 1
        
        while idx >= 0 and s[idx] != " ":
            len_of_last += 1
            idx -= 1
        
        return len_of_last
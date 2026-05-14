class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_chars = [0] * 26

        for idx in range(len(s)):
            s_idx = ord(s[idx]) - ord('a')
            t_idx = ord(t[idx]) - ord('a')
            count_chars[s_idx] += 1
            count_chars[t_idx] -= 1
        
        return all(num == 0 for num in count_chars)
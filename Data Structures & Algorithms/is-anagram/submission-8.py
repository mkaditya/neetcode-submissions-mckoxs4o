class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for idx in range(len(s)):
            s_idx, t_idx = ord(s[idx]) - ord('a'), ord(t[idx]) - ord('a')
            count[s_idx] += 1
            count[t_idx] -= 1
        
        return not any(count)
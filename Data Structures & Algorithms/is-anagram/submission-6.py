class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for idx in range(len(s)):
            s_count_idx = ord(s[idx]) - ord('a')
            t_count_idx = ord(t[idx]) - ord('a')
            count[s_count_idx] += 1
            count[t_count_idx] -= 1
        
        return not any(ct !=0 for ct in count)
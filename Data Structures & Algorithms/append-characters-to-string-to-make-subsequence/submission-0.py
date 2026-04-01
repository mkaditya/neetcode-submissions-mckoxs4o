class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_idx = 0
        t_len = len(t)
        for idx in range(len(s)):
            if s[idx] == t[t_idx]:
                t_idx += 1
            if t_idx == t_len:
                break
        return t_len - t_idx
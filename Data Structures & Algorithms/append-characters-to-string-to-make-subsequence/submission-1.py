class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # t should be subsequenc of s, we can modify s
        # coadching , coding
        # co,d
        # cocoaching

        s_len, t_len = len(s), len(t)
        s_idx, t_idx = 0, 0

        while s_idx < s_len and t_idx < t_len:

            if s[s_idx] == t[t_idx]:
                s_idx += 1
                t_idx += 1
            else:
                s_idx += 1

        return t_len - t_idx
            
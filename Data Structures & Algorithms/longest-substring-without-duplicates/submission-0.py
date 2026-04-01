class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for idx in range(len(s)):
            curr_val = s[idx]
            if curr_val in mp:
                l = max(l, mp[curr_val] + 1) # ensure safe l, don't look backwards
            mp[curr_val] = idx
            res = max(res, idx - l + 1)
        return res
            
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for idx in range(len(prefix)):
            curr_char = prefix[idx]
            for s in strs[1:]:
                if idx >= len(s) or s[idx] != curr_char:
                    return prefix[:idx]
        return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        for idx in range(len(first_word)):
            curr_char = first_word[idx]
            for s in strs[1:]:
                if idx >= len(s) or s[idx] != curr_char:
                    return first_word[:idx]
        return first_word

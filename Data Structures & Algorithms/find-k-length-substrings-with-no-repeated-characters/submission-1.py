class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        no_rep_str = 0
        char_count = defaultdict(int)

        for idx in range(k):
            char_count[s[idx]] += 1
        
        if len(char_count) == k:
            no_rep_str += 1

        for idx in range(k, len(s)):
            leaving_char, adding_char = s[idx - k], s[idx]
            char_count[leaving_char] -= 1
            char_count[adding_char] += 1

            if char_count[leaving_char] == 0:
                del char_count[leaving_char]
            if len(char_count) == k:
                no_rep_str += 1

        return no_rep_str
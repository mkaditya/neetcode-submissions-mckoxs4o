class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        budget = k
        start_idx, best = 0, 0
        char_count = defaultdict(int)

        for idx, ch in enumerate(s):
            char_count[ch] += 1
            while len(char_count) > k:
                curr_char = s[start_idx]
                char_count[curr_char] -= 1
                if char_count[curr_char] == 0:
                    del char_count[curr_char]
                start_idx += 1
            best = max(best, idx - start_idx + 1)
        return best
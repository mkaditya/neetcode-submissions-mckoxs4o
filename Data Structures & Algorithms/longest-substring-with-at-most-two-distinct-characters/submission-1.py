class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        budget = 2
        char_count = defaultdict(int)
        start_idx, best = 0, 0

        for idx, ch in enumerate(s):
            char_count[ch] += 1
            while len(char_count) > budget:
                curr_char = s[start_idx]
                char_count[curr_char] -= 1
                if char_count[curr_char] == 0:
                    del char_count[curr_char]
                start_idx += 1
            best = max(best, idx - start_idx + 1)
        return best
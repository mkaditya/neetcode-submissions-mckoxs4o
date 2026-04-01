class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        chars = range(ord('A'),ord('Z') + 1)
        max_len = 0
        left_idx = 0
        max_freq = 0
        for right_idx in range(len(s)):
            char_freq[s[right_idx]] = char_freq.get(s[right_idx], 0) + 1
            max_freq = max(max_freq, char_freq[s[right_idx]])
            window_size = right_idx - left_idx + 1
            if window_size - max_freq <= k:
                max_len = max(max_len, window_size)
            else:
                char_freq[s[left_idx]] -= 1
                left_idx += 1
        return max_len

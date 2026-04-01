class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        window_size = len(s1)
        s1_freq = self._freq_count(s1)
        s2_freq = self._freq_count(s2[:window_size])

        matching_chars = sum(1 for idx in range(26) if s1_freq[idx] == s2_freq[idx])
        left = 0
        for right in range(window_size, len(s2)):
            if matching_chars == 26:
                return True
            
            # add char to index
            char_idx = ord(s2[right]) - ord('a')
            s2_freq[char_idx] += 1
            if s2_freq[char_idx] == s1_freq[char_idx]:
                matching_chars += 1
            elif s2_freq[char_idx] - 1 == s1_freq[char_idx]:
                matching_chars -= 1

            # move window
            char_idx = ord(s2[left]) - ord('a')
            s2_freq[char_idx] -= 1
            if s2_freq[char_idx] == s1_freq[char_idx]:
                matching_chars += 1
            elif s2_freq[char_idx] + 1 == s1_freq[char_idx]:
                matching_chars -= 1
            left += 1
        return matching_chars == 26
            

    def _freq_count(self, s: str) -> list[int]:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        return freq
    
    

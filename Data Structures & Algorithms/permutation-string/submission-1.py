class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_char_count = [0] * 26
        s2_char_count = [0] * 26

        for idx in range(len(s1)):
            s1_char_idx = ord(s1[idx]) - ord('a')
            s1_char_count[s1_char_idx] += 1

            s2_char_idx = ord(s2[idx]) - ord('a')
            s2_char_count[s2_char_idx] += 1
        
        matches = 0
        for idx in range(26):
            if s1_char_count[idx] == s2_char_count[idx]:
                matches += 1

        left_idx = 0
        for idx in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            s2_char_idx = ord(s2[idx]) - ord('a')
            s2_char_count[s2_char_idx] += 1

            if s1_char_count[s2_char_idx] == s2_char_count[s2_char_idx]:
                matches += 1
            elif s1_char_count[s2_char_idx] + 1 == s2_char_count[s2_char_idx]: # drifting apart
                matches -= 1

            # move the sliding window
            left_idx_char = ord(s2[left_idx]) - ord('a')
            s2_char_count[left_idx_char] -= 1
            if s1_char_count[left_idx_char] == s2_char_count[left_idx_char]:
                matches += 1 # due to drift there is a match
            if s1_char_count[left_idx_char] - 1 == s2_char_count[left_idx_char]:
                matches -= 1
            left_idx += 1
        return matches == 26
            
        
        
            

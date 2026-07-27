class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26
        for idx in range(len(s)):
            counts[ord(s[idx]) - ord('a')] += 1
            counts[ord(t[idx]) - ord('a')] -= 1
        return all(count == 0 for count in counts)
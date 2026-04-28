class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len1, len2 = len(s), len(t)
        if len1 > len2:
            return self.isOneEditDistance(t, s)
        
        if len2 - len1 > 1:
            return False
        
        for idx in range(len1):
            if s[idx] != t[idx]:
                if len1 == len2:
                    return s[idx+1:] == t[idx+1:]
                else:
                    return s[idx:] == t[idx+1:]
        return len2 == len1 + 1
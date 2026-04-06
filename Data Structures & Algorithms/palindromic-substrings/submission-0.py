class Solution:
    def countSubstrings(self, s: str) -> int:
        no_of_palis = 0

        for idx in range(len(s)):
            # odd that is starting from same idx and expanding outwards
            l, r = idx, idx
            while l >=0 and r < len(s) and s[l] == s[r]:
                no_of_palis += 1
                l -= 1
                r += 1
            
            # even that is left & right starting from different points
            l, r = idx, idx + 1
            while l >=0 and r < len(s) and s[l] == s[r]:
                no_of_palis += 1
                l -= 1
                r += 1
        return no_of_palis
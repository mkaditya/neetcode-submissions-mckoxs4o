class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        if not s:
            return palindrome

        def expand_around_center(l,r):
            while l >=0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1
            return s[l+1:r]

        for center in range(len(s)):
            palindrome_odd = expand_around_center(center, center)
            palindrome_even = expand_around_center(center, center+1)
            if len(palindrome) < len(palindrome_odd):
                palindrome = palindrome_odd
            if len(palindrome) < len(palindrome_even):
                palindrome = palindrome_even
        return palindrome    
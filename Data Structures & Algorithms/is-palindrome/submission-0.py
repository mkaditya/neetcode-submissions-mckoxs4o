class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftIdx, rightIdx = 0, len(s) - 1
        
        while leftIdx < rightIdx:

            while leftIdx < rightIdx and not s[leftIdx].isalnum():
                leftIdx += 1

            while leftIdx < rightIdx and not s[rightIdx].isalnum():
                rightIdx -= 1
        
            if s[leftIdx].lower() != s[rightIdx].lower():
                return False
            
            leftIdx += 1
            rightIdx -= 1

        return True

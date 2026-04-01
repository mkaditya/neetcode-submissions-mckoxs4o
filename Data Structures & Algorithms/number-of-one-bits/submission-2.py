class Solution:
    def hammingWeight(self, n: int) -> int:
        # Brian Kernighan's Algorithm
        # When you subtract 1 from a number, 
        # all the bits after (to the right of) the rightmost 1 get flipped.
        """
        res = 0
        while n > 0:
            n = n & (n-1)
            res += 1
        return res
        """
        res = 0
        while n > 0:
            res += 1
            n = n & (n-1) 
        return res
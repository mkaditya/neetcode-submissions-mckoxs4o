class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        # If you right-shift a number by 1 bit, you remove the last bit. 
        # So the count of 1s in the original number equals the count in the shifted number
        # = PLUS the last bit (0 or 1)

        for i in range(1, n+1):
            res[i] = res[i >> 1] + (i & 1)
        return res

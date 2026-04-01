class Solution:
    def hammingWeight(self, n: int) -> int:
        k = 1
        res = 0
        for i in range(32):
            res += 1 if n & 1 else 0
            n = n >> 1
        return res

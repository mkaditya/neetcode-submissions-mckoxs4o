class Solution:
    def hammingWeight(self, n: int) -> int:
        k = 1
        res = 0
        for i in range(32):
            if ((k << i) & n):
                res += 1 
        return res

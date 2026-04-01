class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        fn1 = 1
        fn2 = 2

        for i in range(3, n+1):
            temp = fn1 + fn2
            fn1, fn2  = fn2, temp
        return fn2
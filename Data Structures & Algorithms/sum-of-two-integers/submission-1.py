class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Sum of two integers using only bitwise operations.

        Core insight — binary addition has exactly two parts:
            1 + 1 = 0, carry 1
            1 + 0 = 1, no carry
            0 + 0 = 0, no carry

        XOR gives the sum WITHOUT carry:
            0 ^ 0 = 0,  0 ^ 1 = 1,  1 ^ 1 = 0  ← exactly matches addition

        AND + left shift gives the CARRY:
            only 1 & 1 = 1 (the only case that produces a carry)
            shift left because carry moves one position up

        Example — worst case carry cascade, a=7 (0111), b=1 (0001):
            Round 1: a = 0111 ^ 0001 = 0110  b = (0111 & 0001) << 1 = 0010
            Round 2: a = 0110 ^ 0010 = 0100  b = (0110 & 0010) << 1 = 0100
            Round 3: a = 0100 ^ 0100 = 0000  b = (0100 & 0100) << 1 = 1000
            Round 4: a = 0000 ^ 1000 = 1000  b = 0  → stop, return 8 ✓

        Example — no carry at all, a=4 (100), b=2 (010):
            Round 1: a = 100 ^ 010 = 110  b = (100 & 010) << 1 = 0  → stop, return 6 ✓
            No overlapping 1-bits → no carry → done in one round.

        Python note:
            Python ints are infinite precision — left shifting a negative number
            never terminates. Mask to 32 bits with 0xFFFFFFFF to simulate
            fixed-width arithmetic. After the loop, if bit 31 is set,
            convert back via ~(a ^ mask).

        Time:  O(1) — at most 32 rounds (one per bit position)
        Space: O(1)
        """
        mask = 0xFFFFFFFF # 32 bits
        max_int = 0x7FFFFFFF

        while b & mask:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry
        
        return a if a <= max_int else ~(a ^ mask)

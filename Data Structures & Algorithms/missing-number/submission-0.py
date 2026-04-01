class Solution:
    """
    x ^ x = 0, x ^ 0 = x    
    a ^ b = b ^ a
    (a ^ b) ^ c = a ^ (b ^ c)
    """
    def missingNumber(self, nums: List[int]) -> int:
        xorr = len(nums)
        for i in range(len(nums)):
            xorr = xorr ^ i # xorr of all indices
            xorr = xorr ^ nums[i] # xorr of all numbers
        return xorr # (xorr of all indices) & xorr of all numbers will give missing number
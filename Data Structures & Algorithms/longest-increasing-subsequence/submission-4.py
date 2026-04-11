class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: 
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        return self.nlogn_solution(nums)

    def n2_solution(self, nums):
        dp = [1] * len(nums)
        for idx in range(1, len(nums)):
           for solved_idx in range(idx):
            if nums[solved_idx] < nums[idx]:
                dp[idx] = max(1 + dp[solved_idx], dp[idx])
        
        return max(dp)

    def nlogn_solution(self, nums):
        """
        Maintains a list 'tails' where tails[i] is the smallest ending element 
        of all increasing subsequences of length i+1.
        
        For each num in nums:
        1. Use binary search to find the leftmost element in 'tails' >= num.
        2. If num is larger than all elements, append it (extends the longest sequence).
        3. Otherwise, replace the found element with num (optimizes potential future sequences).
        """
        tails = [] # list of piles tails whic we creat as we progress

        for num in nums:
            tail_pos = self.binary_search(tails, num)
            if tail_pos == len(tails):
                tails.append(num) # all numbers in tails are lower than current value
            else:
                tails[tail_pos] = num # replacing previous big value in subsequence with small value
        return len(tails)

    
    def binary_search(self, tails, num):
        lo, hi = 0, len(tails) - 1
        res = len(tails) # num is greater than everythingin in tails
        while lo <= hi:
            mid = (lo + hi) // 2
            if tails[mid] >= num:
                # found a pile which has greater num, at least this should be remove if we can't find anything else
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res
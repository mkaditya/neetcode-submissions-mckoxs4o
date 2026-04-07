class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0  # Fixed: check s[0] != '0'

        for idx in range(2, len(s) + 1):
            one_digit = int(s[idx-1])
            two_digit = int(s[idx-2:idx])

            if one_digit != 0:
                dp[idx] += dp[idx-1]
            
            if 10 <= two_digit <= 26:
                dp[idx] += dp[idx-2]
        
        return dp[len(s)]
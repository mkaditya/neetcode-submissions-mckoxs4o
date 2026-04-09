class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo_cache = {}
        s1_len = len(text1)
        s2_len = len(text2)

        def dfs(s1_idx, s2_idx):
            if s1_idx == s1_len or s2_idx == s2_len:
                return 0

            if (s1_idx, s2_idx) in memo_cache:
                return memo_cache[(s1_idx, s2_idx)]
            
            if text1[s1_idx] == text2[s2_idx]:
                memo_cache[(s1_idx, s2_idx)] = 1 + dfs(s1_idx + 1, s2_idx + 1)
            else:
                memo_cache[(s1_idx, s2_idx)] = max(dfs(s1_idx+1, s2_idx), dfs(s1_idx, s2_idx+1))
            return memo_cache[(s1_idx, s2_idx)]
        
        return dfs(0,0)
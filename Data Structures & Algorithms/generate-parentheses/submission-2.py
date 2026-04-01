class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
      dp: List[List[str]] = [[] for _ in range(n+1)]
      dp[0] = [""]

      for total_pairs in range(1, n+1):
        current_list = []
        for open_pairs in range(total_pairs):
            close_pairs = total_pairs - 1 - open_pairs
            for left in dp[open_pairs]:
                for right in dp[close_pairs]:
                    current_list.append(f"({left}){right}")
        dp[total_pairs] = current_list
      return dp[n]

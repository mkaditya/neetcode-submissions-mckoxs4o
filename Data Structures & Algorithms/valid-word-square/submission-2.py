class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        row_len = len(words)
        
        for row_idx in range(row_len):
            col_len = len(words[row_idx])
            for col_idx in range(col_len):
                if col_idx >= row_len or row_idx >= len(words[col_idx]):
                    return False
                if words[row_idx][col_idx] != words[col_idx][row_idx]:
                    return False
        return True

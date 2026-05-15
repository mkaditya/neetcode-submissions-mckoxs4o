class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        start_idx, end_idx = 0, 0
        while end_idx < len(s):
            while s[end_idx] != '#':
                end_idx += 1
            
            len_str = int(s[start_idx:end_idx])
            word_start = end_idx + 1
            word_end = word_start + len_str
            res.append(s[word_start:word_end])
            start_idx, end_idx = word_end, word_end + 1
        return res


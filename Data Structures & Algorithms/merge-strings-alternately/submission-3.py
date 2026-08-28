class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_len, w2_len = len(word1), len(word2)
        res = []

        w1_idx, w2_idx = 0, 0
        while w1_idx < w1_len and w2_idx < w2_len:
            res.append(word1[w1_idx])
            res.append(word2[w2_idx])
            w1_idx += 1
            w2_idx += 1
        
        res.append(word1[w1_idx:])
        res.append(word2[w2_idx:])
        return "".join(res)
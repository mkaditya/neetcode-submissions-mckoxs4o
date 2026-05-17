class Solution:
    def __init__(self):
        self.delim = "#"

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += str(l) + self.delim + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        start  = 0
        while start < len(s):
            end = start
            while s[end] != self.delim:
                end += 1
            l_of_s = int(s[start:end])
            word_start = end + 1
            word_end = word_start + l_of_s
            res.append(s[word_start:word_end])
            start = word_end
        return res
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start_idx, end_idx = 0, 0
        while end_idx < len(s):
            while s[end_idx] != "#":
                end_idx += 1
            length = int(s[start_idx:end_idx])
            start_idx = end_idx + 1 
            end_idx = start_idx + length
            res.append(s[start_idx:end_idx])
            start_idx = end_idx
        return res


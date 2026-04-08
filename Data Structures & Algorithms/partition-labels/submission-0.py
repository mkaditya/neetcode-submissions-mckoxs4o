class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = defaultdict(int)
        for idx, c in enumerate(s):
            last_seen[c] = idx
        
        result = []
        start, end = 0, 0
        for idx, c in enumerate(s):
            last_idx = last_seen[c]
            end = max(end, last_idx)
            if end == idx:
                result.append(end - start + 1)
                start = end + 1
        return result
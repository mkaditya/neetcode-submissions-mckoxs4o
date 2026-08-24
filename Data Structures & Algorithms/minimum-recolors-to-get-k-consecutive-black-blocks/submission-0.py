class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if not blocks or len(blocks) < k:
            return -1 

        w_count = 0
        for idx in range(k):
            if blocks[idx] == "W":
                w_count += 1
            
        min_swaps = w_count
        for idx in range(k, len(blocks)):
            leaving_char = blocks[idx - k]
            if leaving_char == "W":
                w_count -= 1
            if blocks[idx] == "W":
                w_count += 1
            min_swaps = min(min_swaps, w_count)
        
        return min_swaps
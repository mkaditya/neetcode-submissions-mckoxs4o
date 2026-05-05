class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = defaultdict(int)
        for ch in s:
            char_count[ch] += 1
        
        max_heap = []
        for ch, count in char_count.items():
            max_heap.append([count, ch])
        
        heapq.heapify_max(max_heap)

        prev = None
        res = ""

        while max_heap or prev:
            if not max_heap: # repeating chars next to eac other
                return ""
            count, ch = heapq.heappop_max(max_heap)
            res += ch
            count -= 1
            
            if prev:
                heapq.heappush_max(max_heap, prev)
            
            if count > 0:
                prev = [count, ch]
            else:
                prev = None
        return res + prev[1] if prev else res
        
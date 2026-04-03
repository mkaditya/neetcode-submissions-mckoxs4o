class SlidingWindow:
    def __init__(self, s:str, t: str):
        self.s, self.t = s, t
        self.need = Counter(t)
        self.window = defaultdict(int)
        self.left, self.satisfied = 0, 0
        self.min_window_len = float("inf")
        self.min_window_left = 0

    
    def expand(self, c: str):
        self.window[c] += 1
        if c in self.need and self.window[c] == self.need[c]:
            self.satisfied += 1 # we found target char count matcic the needs
    
    def is_valid_window(self):
        return self.satisfied == len(self.need)

    
    def contract(self, right: int):
        while self.is_valid_window():
            window_size = right - self.left + 1
            if window_size < self.min_window_len:
                self.min_window_len = window_size
                self.min_window_left = self.left
            self.remove_left()
    
    def remove_left(self):
        left_char = self.s[self.left]
        if left_char in self.need and self.window[left_char] == self.need[left_char]:
            self.satisfied -= 1
        self.window[left_char] -= 1
        self.left += 1

    def result(self):
        if self.min_window_len == float("inf"):
            return ""
        return self.s[self.min_window_left : self.min_window_left + self.min_window_len]

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        sw = SlidingWindow(s, t)
        for idx, char in enumerate(s):
            sw.expand(char)
            sw.contract(idx)
        return sw.result()
        

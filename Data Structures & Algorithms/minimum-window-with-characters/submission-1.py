from collections import Counter, defaultdict


class SlidingWindow:
    def __init__(self, s: str, t: str):
        self.s = s
        self.need = Counter(t)           # target char frequencies e.g. {X:1, Y:1, Z:1}
        self.window = defaultdict(int)   # current window char frequencies
        self.left = 0                    # left pointer of the window
        self.satisfied = 0               # # of unique chars whose frequency requirement is met
        self.min_window_len = float("inf")
        self.min_window_left = 0         # start index of the best window found so far

    def expand(self, c: str):
        # grow window by adding the new right character
        self.window[c] += 1
        # check if this char's count just hit the required amount
        if c in self.need and self.window[c] == self.need[c]:
            self.satisfied += 1

    def is_valid_window(self) -> bool:
        # window is valid when all unique chars in t are fully satisfied
        return self.satisfied == len(self.need)

    def contract(self, right: int):
        # shrink from the left as long as the window remains valid,
        # recording the minimum each time before shrinking
        while self.is_valid_window():
            window_size = right - self.left + 1
            if window_size < self.min_window_len:
                self.min_window_len = window_size
                self.min_window_left = self.left
            self.remove_left()

    def remove_left(self):
        left_char = self.s[self.left]
        # check BEFORE decrementing — if we're exactly at the required count,
        # removing this char will break satisfaction for this character
        if left_char in self.need and self.window[left_char] == self.need[left_char]:
            self.satisfied -= 1
        self.window[left_char] -= 1
        self.left += 1

    def result(self) -> str:
        # if min_window_len was never updated, no valid window was found
        if self.min_window_len == float("inf"):
            return ""
        return self.s[self.min_window_left : self.min_window_left + self.min_window_len]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        sw = SlidingWindow(s, t)
        for idx, char in enumerate(s):
            sw.expand(char)    # move right pointer: add one char to window
            sw.contract(idx)   # move left pointer: shrink while window is valid
        return sw.result()
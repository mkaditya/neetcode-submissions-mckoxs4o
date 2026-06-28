class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def populate(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.count += 1

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        return curr.count

    def prefixCount(self, words: List[str], pref: str) -> int:
        for word in words:
            self.populate(word)
        return self.search(pref)
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True


    def _traverse(self, s: str) -> TrieNode:
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None
        
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            c_val = ord(c) - ord('a')
            if node.children[c_val] == None:
                node.children[c_val] = TrieNode()
            node = node.children[c_val]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            c_val = ord(c) - ord('a')
            if node.children[c_val] == None:
                return False
            node = node.children[c_val]
        return node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            c_val = ord(c) - ord('a')
            if node.children[c_val] == None:
                return False
            node = node.children[c_val]
        return True

        
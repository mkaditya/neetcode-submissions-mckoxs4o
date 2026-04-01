class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    
    def search(self, word: str) -> bool:

        def find(start_idx, node):
            if start_idx >= len(word):
                return node.is_word
            char = word[start_idx]
            for idx in range(start_idx, len(word)):
                if char == ".":
                    for child in node.children.values():
                        if find(start_idx+1, child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    return find(start_idx + 1,  node.children[char])
            return False
        
        return find(0, self.root)
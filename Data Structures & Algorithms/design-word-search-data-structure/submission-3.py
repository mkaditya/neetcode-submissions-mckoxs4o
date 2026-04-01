class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()


    def search(self, word: str) -> bool:
        def search_from(node, word):
            for idx, char in enumerate(word):
                if char == ".":
                    return any(search_from(child, word[idx+1:]) for child in node.children.values())
                elif char not in node.children:
                    return False
                else:
                    node = node.children[char]
            return node.is_word
        
        return search_from(self.root, word)

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

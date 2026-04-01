class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
        

    def search(self, word: str) -> bool:

        def search_dfs(node, idx):
            if idx == len(word):
                return node.end_of_word

            char = word[idx]

            if not char: return False

            if char == ".":
                return any(search_dfs(child, idx + 1) for child in node.children.values())
            else:
                if char not in node.children:
                    return False
                return search_dfs(node.children[char], idx +1)
        
        return search_dfs(self.root, 0)
        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search_word(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.add_word(word)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def find_word(node,r,c,curr_word):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or not node or not node.children:
                return

            char = board[r][c]
            if char not in node.children:
                return
            
            visited.add((r,c))
            node = node.children[char]
            curr_word  += char
            if node.is_word:
                res.add(curr_word)

            find_word(node, r, c+1, curr_word)
            find_word(node, r, c-1, curr_word)
            find_word(node, r+1, c, curr_word)
            find_word(node, r-1, c, curr_word)

            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                find_word(self.root, r, c, "")
        return list(res)
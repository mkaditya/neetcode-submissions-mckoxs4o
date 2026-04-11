class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
    
    def search(self, s, i , j):
        node = self.root
        for idx in range(i, j+1):
            if s[idx] not in node.children:
                return False
            node = node.children[s[idx]]
        return node.is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # to capture out of bounds

        max_word_len = 0
        for word in wordDict:
            max_word_len = max(max_word_len, len(word))

        for i in reversed(range(len(s))):
            for j in range(i, min(len(s), i + max_word_len)):
                if trie.search(s, i, j) and dp[j+1]: # i.e there is valid from i,j and j+1 ..end
                    dp[i] = True
                    break
        return dp[0]

        

class TrieNode:
    def __init__(self):
        self.pairs = {}
        self.word_count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def populate(self, word):
        curr = self.root
        count = 0
        for idx in range(len(word)):
            right_idx = len(word) - 1 - idx
            if (word[idx], word[right_idx]) not in curr.pairs:
                curr.pairs[(word[idx], word[right_idx])] = TrieNode()          
            curr = curr.pairs[(word[idx], word[right_idx])]
            count += curr.word_count
        curr.word_count += 1
        return count

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for word in words:
            count += self.populate(word)
        return count
        

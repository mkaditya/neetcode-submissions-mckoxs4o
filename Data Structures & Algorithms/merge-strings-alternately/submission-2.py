class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        small_word, large_word = word1, word2
        if len(small_word) > len(large_word):
            small_word, large_word = large_word, small_word

        res = ""
        for idx in range(len(small_word)):
            res += word1[idx] + word2[idx]
        
        res += large_word[len(small_word):]
        return res
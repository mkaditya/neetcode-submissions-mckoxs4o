class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def construct_dict(self, dictionary):
        for word in dictionary:
            curr = self.root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.is_word = True

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.construct_dict(dictionary)

        # at each char, exclude and dp of rest are include it as part of word len k, and do dp of ofther
        # dp[i] = 1 + dp[i+1] (if no word)
        #         dp[i+k] (k size word, we need to solve dp of rest of string)
    
        s_len = len(s)
        dp = [0] * (s_len + 1)
        for idx in reversed(range(s_len)):
            # don't include string 
            dp[idx] = 1 + dp[idx+1]

            # evaluate alternate of include string + dp of rest of string
            curr = self.root
            for i in range(idx, s_len):
                if s[i] not in curr.children:
                    break
                curr = curr.children[s[i]]
                if curr.is_word:
                    dp[idx] = min(dp[idx], dp[i + 1])

        return dp[0]
        
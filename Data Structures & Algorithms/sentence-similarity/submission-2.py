class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        similar_words = defaultdict(set)

        for word1, word2 in similarPairs:
            similar_words[word1].add(word2)
            similar_words[word2].add(word1)
        
        for idx in range(len(sentence1)):
            word1, word2 = sentence1[idx], sentence2[idx]
            if word1 == word2:
                continue
            
            if word2 not in similar_words[word1]:
                return False
        
        return True
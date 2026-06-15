class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_len, abbr_len = len(word), len(abbr)
        word_idx, abbr_idx = 0, 0

        while word_idx < word_len and abbr_idx < abbr_len:
            if abbr[abbr_idx].isalpha():
                if abbr[abbr_idx] != word[word_idx]:
                    return False
                abbr_idx += 1
                word_idx += 1
            else:
                if abbr[abbr_idx] == '0':
                    return False
                num = 0
                while abbr_idx < abbr_len and abbr[abbr_idx].isdigit():
                    num = num * 10 + int(abbr[abbr_idx])
                    abbr_idx += 1
                word_idx += num
        return word_idx == word_len and abbr_idx == abbr_len
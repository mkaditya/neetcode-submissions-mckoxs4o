class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_match = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if stack and stack[-1] == bracket_match[c]:
                    stack.pop()
                else:
                    return False
        return not stack
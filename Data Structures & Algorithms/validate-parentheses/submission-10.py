class Solution:
    def isValid(self, s: str) -> bool:
        bracket_match = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []
        for c in s:
            if c in "{([":
                stack.append(c)
            else:
                if stack and stack[-1] == bracket_match[c]:
                    stack.pop()
                else:
                    return False
        return not stack
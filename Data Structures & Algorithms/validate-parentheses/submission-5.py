class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            "}" : "{",
            "]" : "[",
            ")" : "(",
        }
        
        for c in s:
            if not c in closeToOpen:
                stack.append(c)
            else:
                if not stack or not stack[-1] == closeToOpen[c]:
                    return False
                else:
                    stack.pop()
        return not stack
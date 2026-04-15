class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                second_val = stack.pop()
                first_val = stack.pop()
                stack.append(first_val - second_val)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                second_val = stack.pop()
                first_val = stack.pop()
                stack.append(int(first_val / second_val))
            else:
                stack.append(int(token))
        return stack.pop()
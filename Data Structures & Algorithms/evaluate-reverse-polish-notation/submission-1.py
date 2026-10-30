class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["*", "/", "-", "+"]:
                r = stack.pop()
                l = stack.pop()
                if token == "+":
                    stack.append(l + r)
                elif token == "-":
                    stack.append(l - r)
                elif token == "*":
                    stack.append(l * r)
                elif token == "/":
                    stack.append(int(l / r))
            else:
                stack.append(int(token))
        return stack.pop()
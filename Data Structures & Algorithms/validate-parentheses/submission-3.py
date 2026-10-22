class Solution:
    def isValid(self, s: str) -> bool:
        stash = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stash.append(char)
            else:
                if len(stash) == 0:
                    return False
                match char:
                    case ")":
                        if (stash.pop() != '('):
                            return False
                    case "}":
                        if (stash.pop() != '{'):
                            return False
                    case "]":
                        if (stash.pop() != '['):
                            return False
        return len(stash) == 0
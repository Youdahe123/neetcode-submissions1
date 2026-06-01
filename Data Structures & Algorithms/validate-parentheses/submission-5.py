class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}":"{",")":"(","]":"["}
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack and pairs[char] == stack[-1]:
                        stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False

        
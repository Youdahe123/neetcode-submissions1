class Solution:
    def isValid(self, s: str) -> bool:

        parths = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack = []


        for i in s:
            if i not in "}])":
                stack.append(i) # ["])}"]
            else:
                if stack and stack[-1] == parths[i]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False

        
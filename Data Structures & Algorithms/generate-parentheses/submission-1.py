class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        res = []
        stack = []


        def backtrack(open1,closed1):
            if open1 == n and closed1 == n:
                res.append("".join(stack))
                return
            if closed1 > open1:
                return
            if open1 < n:
                stack.append("(")
                backtrack(open1 + 1,closed1)
                stack.pop()
            if closed1 < open1:
                stack.append(")")
                backtrack(open1,closed1+1)
                stack.pop()
        backtrack(0,0)
        return res
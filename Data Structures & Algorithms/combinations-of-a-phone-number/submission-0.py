class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }


        def backtrack(index,combo):
            if len(combo) == len(digits):
                res.append("".join(combo))
                return 
            for char in digitToChar[digits[index]]:
                combo.append(char)
                backtrack(index + 1,combo)
                combo.pop()

        if digits:
            backtrack(0,[])
        return res

        
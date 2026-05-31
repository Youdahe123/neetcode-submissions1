class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = {}
        T = {}

        for i in s:
            if i not in S:
                S[i] = 0
            else:
                S[i] += 1
        for j in t:
            if j not in T:
                T[j] = 0
            else:
                T[j] += 1
        return S == T
        
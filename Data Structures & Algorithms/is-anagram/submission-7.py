from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s = Counter(s)
        f = Counter(t)
        return s == f
        
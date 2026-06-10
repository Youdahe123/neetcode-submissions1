class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        #{} r: 2
        #   a: 2
        if len(s) != len(t):
            return False
        Scount = {}
        Tcount = {}
        for i in range(len(s)):
            Scount[s[i]] = 1 + Scount.get(s[i], 0)
            Tcount[t[i]] = 1 + Tcount.get(t[i], 0)
        return Scount == Tcount

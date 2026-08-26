from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not(t):
            return " "
        counterT = Counter(t)
        window = {}
        have = 0
        need = len(counterT)
        res = [-1,-1]
        resLen = float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in counterT and counterT[c] == window[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in counterT and counterT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        return s[res[0] : res[1] + 1] if resLen != float('inf') else ""
        
        
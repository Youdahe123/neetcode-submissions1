class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        replace = {}
        l = 0
        longest = 0 

        for r in range(len(s)):
            replace[s[r]] = 1 + replace.get(s[r],0)

            while (r-l + 1) - max(replace.values()) > k:
                replace[s[l]] -= 1
                l += 1
            longest = max(longest,(r-l + 1))
        return longest
        
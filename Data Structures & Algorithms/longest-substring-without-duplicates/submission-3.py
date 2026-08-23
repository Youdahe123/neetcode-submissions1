class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        currLongest = 0
        words = set()

        for r in range(len(s)):
            while s[r] in words:
                words.remove(s[l])
                l += 1
            words.add(s[r])
            currLongest = max(currLongest,r - l + 1)
        return currLongest

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        currSet = set()
        maxLength = 0

        for right in range(len(s)):
            while s[right] in currSet:
                currSet.remove(s[l])
                l += 1
            currSet.add(s[right])
            maxLength = max(maxLength,len(s[l:right]) + 1)
        return maxLength


        
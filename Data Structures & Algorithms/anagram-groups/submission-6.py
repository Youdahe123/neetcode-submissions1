class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord('a') - ord(letter)] += 1
            res[tuple(count)].append(word)
        return list(res.values())
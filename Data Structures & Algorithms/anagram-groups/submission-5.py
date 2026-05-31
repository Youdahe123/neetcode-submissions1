class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for word in s:
                count[ord("a") - ord(word)] += 1
            res[tuple(count)].append(s)
        return list(res.values())

        
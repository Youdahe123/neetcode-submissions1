class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)


        for word in strs:
            count = [0] * 26 # this makes a array of 26 0's

            for letter in word:
                count[ord(letter)- ord('a')] += 1
            
            
            res[tuple(count)].append(word)
        
        
        return list(res.values())
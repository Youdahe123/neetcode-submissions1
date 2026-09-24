class Solution:
    def partition(self, s: str) -> List[List[str]]:


        sub = []
        res = []

        def backtrack(index):
            if index == len(s):
                res.append(sub.copy())
                return
            
            for end in range(index,len(s)):
                if s[index:end + 1] == s[index:end + 1][::-1]:
                    sub.append(s[index:end + 1])
                    backtrack(end + 1)
                    sub.pop()
                else:
                    continue
        backtrack(0)
        return res

        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        sub  = []
        used = set()
        res = []

        def dfs(index):
            if len(sub) == len(nums) :
                res.append(sub.copy())
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                sub.append(nums[i])
                dfs(i)
                sub.pop()
                used.remove(i)

        dfs(0)
        return res
        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        
        candidates.sort()


        def dfs(index,curr,total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or index == len(candidates):
                return 

            # include the element at candidate[index]
            curr.append(candidates[index])
            dfs(index + 1, curr, total + candidates[index])
            curr.pop()
            # skip the element at candidate[index]
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            dfs(index + 1,curr,total)
        dfs(0,[],0)
        return res

        
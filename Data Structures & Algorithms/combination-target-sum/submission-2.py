class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        sub = []


        def backtrack(index,currSum):
            if currSum > target:
                return
            if currSum == target:
                res.append(sub.copy())
                

            for i in range(index,len(nums)):

                sub.append(nums[i])
                backtrack(i,currSum + nums[i])
                sub.pop()
        backtrack(0,0)
        return res

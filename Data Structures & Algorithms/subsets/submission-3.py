class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:



        sub = []
        res = []

        def backtrack(index):
            if index == len(nums):
                res.append(sub.copy())
                return
            # includes
            sub.append(nums[index])
            backtrack(index + 1)
            sub.pop()

            backtrack(index + 1)
        backtrack(0)
        return res
            # excludes


        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        sub = []

        def backtrack(index):
            if len(nums) == index:
                res.append(sub.copy())
                return
            sub.append(nums[index])
            backtrack(index + 1)
            sub.pop()
            backtrack(index + 1)
        backtrack(0)
        return res
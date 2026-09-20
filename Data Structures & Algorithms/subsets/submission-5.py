class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:



        sub = []
        res = []


        def backtrack(index):
            # base case when we reach end of decision tree
            if index == len(nums):
                res.append(sub.copy())
                return 
            # including the number in subset

            sub.append(nums[index])
            backtrack(index + 1)
            sub.pop()

            backtrack(index + 1)
        backtrack(0)
        return res
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:



        sub = []
        nums.sort()
        res = []

        def backtrack(index):
            if index == len(nums):
                res.append(sub.copy())
                return
            

            sub.append(nums[index])
            backtrack(index + 1)
            sub.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1)
                
        backtrack(0)
        return res
        
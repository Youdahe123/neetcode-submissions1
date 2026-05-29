class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # start = 1
        # sumofNum = [start := start * x for x in nums] # brute force

        # res = [int(start/i) for i in nums  ]
        # return res
        # we need to do prefix postfix then basically add them7
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)): # for each in res array  
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


            # [1,2,4,6]
            # [1,1,1,1] prefix = 1
            # [1,1,1,1] prefix = 1 nums[i] = 1
            # [1,1,1,1] prefix = 2  nums[i] = 2
            # [1,1,2,1] prefix = 8 nums[i] = 4
            # [1,1,2,8] prefix = 24 nums[i] = 6
            # [1,1,2,8]
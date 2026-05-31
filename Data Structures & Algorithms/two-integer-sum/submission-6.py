class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}

        for index,value in enumerate(nums):
            difference = target - value
            if difference in h:
                return [h[difference],index]
            else:
                h[value] = index
        
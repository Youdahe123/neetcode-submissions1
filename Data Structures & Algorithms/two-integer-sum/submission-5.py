class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        difference = {}

        for i in range(len(nums)):
            differenceNumber = target - nums[i]
            if differenceNumber in difference:
                return [difference[differenceNumber],i]  
            difference[nums[i]] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSet = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in numsSet:
                return [numsSet[pair], i]
            numsSet[nums[i]] = i
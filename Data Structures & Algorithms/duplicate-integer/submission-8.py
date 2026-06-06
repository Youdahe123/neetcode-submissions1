class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set(nums) = 1, 2, 3
        #len(set(nums)) == len(nums)
        return len(set(nums)) != len(nums)
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLength = 0

        for i in nums:
            if i - 1 not in numsSet:
                length = 1
                while i + length in numsSet:
                    length += 1
                maxLength = max(maxLength,length)
        return maxLength
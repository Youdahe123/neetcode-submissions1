class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # a set that holds each number check while the - 1 version is still within the set if it is we incrase the length and then add that numeber to set if its not then we add it to set 
        # set anywas as that length reseting lenght every time
        numsset = set(nums)
        maxLength = 0

        for num in nums:
            if num - 1 not in numsset:
                length = 1
                while num + length in numsset:
                    length += 1              
                maxLength = max(maxLength,length)
        return maxLength
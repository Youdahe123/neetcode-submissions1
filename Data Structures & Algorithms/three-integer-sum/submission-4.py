class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        for index,currNum in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1

            while left < right:
                if nums[index] + nums[left] + nums[right] == 0:
                    res.append([nums[index],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[index] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        
        return res

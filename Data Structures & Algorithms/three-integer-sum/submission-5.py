class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Sort first so two pointer technique works (we need direction)
        nums.sort()
        res = []

        for index, currNum in enumerate(nums):

            # Skip duplicate values for the fixed pointer
            # to avoid returning the same triplet twice
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            # Two pointers start just after index and at the end
            left = index + 1
            right = len(nums) - 1

            while left < right:
                total = nums[index] + nums[left] + nums[right]

                if total == 0:
                    # Found a valid triplet, add to result
                    res.append([nums[index], nums[left], nums[right]])

                    # Skip duplicate values for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicate values for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward after processing triplet
                    left += 1
                    right -= 1

                elif total > 0:
                    # Sum too big, move right pointer left to get smaller number
                    right -= 1

                else:
                    # Sum too small, move left pointer right to get bigger number
                    left += 1

        return res
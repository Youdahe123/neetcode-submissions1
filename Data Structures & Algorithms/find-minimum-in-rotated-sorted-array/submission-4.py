class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        currMin =nums[0]

        while low <= high:
            if nums[low] < nums[high]:
                currMin = min(currMin, nums[low])
                break
            mid = (low + high) // 2
            currMin = min(currMin,nums[mid])

            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return currMin
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1


        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]: # left half is sorted
                if nums[mid] >= target >= nums[low]: # the target is within the left half
                    high = mid - 1
                else:
                    low = mid + 1
            else: # right half is sorted
                if nums[high] >= target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # have a left and a right
        # if the sum of the numbers is bigger than the target move the right inwards if its to small. move thje left inwards


        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            if numbers[left] + numbers[right] > target:
                right -=1
            elif numbers[left] + numbers[right] < target:
                left += 1
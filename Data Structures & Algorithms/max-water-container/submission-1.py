class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # have a left pointer 
        left = 0
        right = len(heights) - 1
        maxHeight = 0
        while left < right:
            water = (right - left) * min(heights[right],heights[left])
            maxHeight = max(maxHeight,water)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxHeight
        
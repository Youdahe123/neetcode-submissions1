class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] # stores (height, start_index) pairs
        maxArea = 0

        for height in range(len(heights)):
            # assume current bar starts at its own index
            start = height

            # when we find a shorter bar, pop taller bars and calculate their areas
            # a taller bar can't extend past a shorter bar to its right
            while stack and stack[-1][0] > heights[height]: 
                poppedHeight, poppedindex = stack.pop()
                # width = distance from popped bar's start to current index
                area = (height - poppedindex) * poppedHeight
                # current bar inherits the popped bar's start index
                # meaning it can stretch back to where the popped bar started
                start = poppedindex
                maxArea = max(maxArea, area)

            # push current bar with its (possibly extended) start index
            stack.append((heights[height], start))

        # leftover bars in stack never hit a shorter bar to their right
        # so they can stretch all the way to the end of the array
        for height, index in stack:
            maxArea = max(maxArea, (len(heights) - index) * height)

        return maxArea
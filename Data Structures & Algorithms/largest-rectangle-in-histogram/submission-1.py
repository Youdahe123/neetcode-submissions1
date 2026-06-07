class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] ## (height,index)
        maxArea = 0

        for height in range(len(heights)):
            start = height
            while stack and stack[-1][0] > heights[height]: 
                poppedHeight,poppedindex = stack.pop()
                area = (height - poppedindex) * poppedHeight
                start = poppedindex
                maxArea = max(maxArea,area)
            stack.append((heights[height],start))
   
        print(stack)

        for height,index in stack:
            maxArea = max(maxArea,(len(heights) - index) * height)
        return maxArea
        # if (len(heights) - stack[-1][-1]) * stack[-1][0] > maxArea:
        #     maxArea = (len(heights) - stack[-1][-1]) * stack[-1][0]
        # return maxArea
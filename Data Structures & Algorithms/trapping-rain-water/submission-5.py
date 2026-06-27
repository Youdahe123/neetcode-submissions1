class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]

        for i in range(1,len(height)):
            leftMax[i] = max(leftMax[i - 1],height[i])

        for j in range(len(height) - 2,-1,-1):
            rightMax[j] = max(rightMax[j + 1],height[j])
        
        water = 0

        for x in range(len(height)):
            water += min(leftMax[x],rightMax[x]) - height[x]
        return water

        
        
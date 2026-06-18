class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)
        maxL[0] = height[0]
        maxR[len(height) - 1] = height[len(height) - 1]

        for i in range(1,len(height)):
            maxL[i] = max(maxL[i-1],height[i])
        
        for i in range(len(height)-2,-1,-1):
            maxR[i] = max(maxR[i+1],height[i])

        water = 0

        for i in range(len(height)):
            water += max(0,min(maxL[i],maxR[i]) - height[i])
        
        return water
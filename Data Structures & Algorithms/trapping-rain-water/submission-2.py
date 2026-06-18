class Solution:
    def trap(self, height: List[int]) -> int:
        # continues max L and a Max Right
        # then basiocally we are going to let the maxL to be a list of all the maxes seen on the left up to that point
        # the maxRight will be the array of all the maxes seen up to that point on the right
        # and at each check we will compute the water by saying min of the 2 maxs - the current height is how much water we can add

        maxL = [0] * len(height)
        maxR = [0] * len(height)

        maxL[0] = height[0]
        maxR[len(height) - 1] = height[len(height)  - 1]

        water = 0

        for i in range(1,len(height)):
            maxL[i] = max(height[i] , maxL[i-1])
        
        for j in range(len(height) - 2 , -1 ,-1):
            maxR[j] = max(height[j],maxR[j + 1])
        
        for space in range(len(height)):
            water += max(0,min(maxL[space],maxR[space]) - height[space])
        
        return water
        
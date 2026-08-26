import collections 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = 0 
        r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r+= 1
        return output

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = []
        # window = []

        # for num in range(k): # first iteration
        #     window.append(nums[num])
        # res.append(max(window))

        # for char in range(k , len(nums)):
        #     window = window[1 : ] # new window becomes everything but the first number 
        #     window.append(nums[char])
        #     res.append(max(window))
        # return res
        
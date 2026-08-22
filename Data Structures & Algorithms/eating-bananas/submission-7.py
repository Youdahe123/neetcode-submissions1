import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r



        while l <= r:
            mid = (l + r) // 2 # current speed
            current = 0 # total time

            for x in piles:
                current += math.ceil(x / mid)

            if current <= h : # koko is eating to 
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        return res


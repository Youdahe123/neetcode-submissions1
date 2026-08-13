import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high


        while low<=high:
            mid = (low + high) // 2
            current = 0

            for i in piles:
                current += math.ceil(i / mid)
            if current <= h:
                res = min(res,mid)
                high = mid - 1
            elif current > h :
                 low = mid + 1
        return res

        
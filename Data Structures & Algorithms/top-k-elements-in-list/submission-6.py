from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        res = []

        for i in counts:
            heapq.heappush(heap,(counts[i],i))

            if len(heap) > k:
                heapq.heappop(heap)
        for c in heap:
            res.append(c[1])
        return res
        
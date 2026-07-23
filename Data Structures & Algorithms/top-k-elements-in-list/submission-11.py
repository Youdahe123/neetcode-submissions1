from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minHeap = []
        for i in count:
            heapq.heappush(minHeap,(count[i],i))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        print(minHeap)
        res = []
        for j in minHeap:
            res.append(j[1])
        return res
        
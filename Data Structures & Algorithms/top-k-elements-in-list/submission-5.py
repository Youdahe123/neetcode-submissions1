class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hash = []
        freq = Counter(nums)
        res = []
        for i in freq:
            heapq.heappush(Hash,(freq[i],i))

            if len(Hash) > k:
                heapq.heappop(Hash)
        for char in Hash:
            res.append(char[1])
        return res
        
        
        
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        cnt = {}

        for n in nums:
            cnt[n] = 1 + cnt.get(n, 0)
        heap = []
        for num, count in cnt.items():
            heapq.heappush(heap, [count, num])
            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for count, num in heap:
            res.append(num)

        return res

            

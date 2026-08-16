import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = []
        pq = []
        for num, freq in c.items():
            heapq.heappush(pq, (-freq, num))

        while k > 0:
            _, num = heapq.heappop(pq)
            res.append(num)
            k -= 1

        return res
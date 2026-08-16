import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in c.items():
            buckets[frequency].append(num)

        res = []

        for frequency in range(len(buckets) - 1, 0, -1):
            for num in buckets[frequency]:
                res.append(num)

                if len(res) == k:
                    return res
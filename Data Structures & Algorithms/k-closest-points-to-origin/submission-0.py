import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        new = zip(points, range(n))
        def distance(point: Tuple(List[int], int)):
            x, y = point[0]
            d = math.sqrt(x ** 2 + y ** 2)
            return (d, point[1])
        indices = list(map((lambda x: x[1]), sorted(map(distance, new))))
        return [points[i] for i in indices[:k]] 

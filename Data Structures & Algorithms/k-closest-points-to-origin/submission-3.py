class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_points = []

        for point in points:
            dist = point[0]**2 + point[1]**2
            dist_to_origin = (dist, [point[0],point[1]])
            heapq.heappush_max(k_points, dist_to_origin)
            if len(k_points) > k:
                heapq.heappop_max(k_points)
        
        res = [point for dist, point in k_points]
        return res
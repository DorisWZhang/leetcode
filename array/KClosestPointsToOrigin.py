class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 08-02-2025
        # given an array of points
        # return array of k points closest to the origin
        # sort by distance and take the first k
        result = []
        point_dist = [(x**2 + y**2) for x, y in points]

        # sort by shortest dist, make sure to update key-val in dict after moving idx
        # selection sort
        for i in range(k):
            minDist = float('inf')
            minIdx = -1
            for j in range(i, len(points)):    
                if point_dist[j] < minDist:
                    minDist = point_dist[j]
                    minIdx = j
    
            # make swap in dict and in points array
            result.append(points[minIdx])
            point_dist[minIdx] = point_dist[i]
            points[minIdx] = points[i]
        return result
             

                
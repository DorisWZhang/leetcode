import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 2025-08-10
        max_heap = [-x for x in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = - heapq.heappop(max_heap)
            stone2 = - heapq.heappop(max_heap)

            if stone1 > stone2:
                stone1 -= stone2
                heapq.heappush(max_heap, -stone1)
            elif stone2 > stone1:
                stone2 -= stone1
                heapq.heappush(max_heap, -stone2)

        if max_heap: # if there is one remaining
            remaining = heapq.heappop(max_heap)
            return -remaining

        return 0
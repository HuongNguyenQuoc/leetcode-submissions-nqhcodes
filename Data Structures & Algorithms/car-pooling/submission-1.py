class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x : x[1])
        heap = []
        curr = 0

        for numPass, frm, t in trips:
            while heap and frm >= heap[0][0]:
                numPassenger = heapq.heappop(heap)[1]
                curr -= numPassenger
            curr += numPass
            if curr > capacity:
                return False
            heapq.heappush(heap, (t, numPass))
        
        return True

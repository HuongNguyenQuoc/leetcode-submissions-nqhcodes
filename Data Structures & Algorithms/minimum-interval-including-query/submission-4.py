class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
      intervals.sort()
      ans, i = {}, 0
      heap = []

      for x in sorted(set(queries)):
        # Tìm tất cả các khoảng có khả năng chứa x và sẽ thêm vào min heap
        while i < len(intervals) and intervals[i][0] <= x:
          l, r = intervals[i]
          heapq.heappush(heap, (r-l+1, r))
          i += 1
        # Remove intervals mà queries đã trôi qua
        while heap and heap[0][1] < x:
          heapq.heappop(heap)
        # Sau khi đã bỏ đi các khoảng unmatch chắc chắn peak của heap sẽ là smallest interval or -1 if heap rỗng
        ans[x] = heap[0][0] if heap else -1
      return [ans[x] for x in queries]
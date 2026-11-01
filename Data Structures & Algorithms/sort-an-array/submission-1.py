class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n: int, i: int) -> None:
            largest = i
            left, right = 2*i+1, 2*i+2

            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
            
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        n = len(nums)

        # Build a max-heap
        for i in range(n//2-1, -1, -1):
            heapify(n, i)

        # Extract elements one by one from the heap
        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(i, 0)
        
        return nums

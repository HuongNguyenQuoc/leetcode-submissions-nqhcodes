class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(array: List[int]) -> List[int]:
            if len(array) <= 1:
                return array
            
            mid = len(array) // 2
            left = merge_sort(array[:mid])
            right = merge_sort(array[mid:])

            return merge(left, right)

        def merge(left: List[int], right: List[int]) -> List[int]:
            res = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
                
            # We need extend the remain both of left and right because when i, j index out of range we
            # need extend the remain of other
            res.extend(left[i:]) # extend left
            res.extend(right[j:]) # extend right

            return res

        merge_sort(nums)
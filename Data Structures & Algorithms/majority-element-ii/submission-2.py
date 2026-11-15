import sys
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 2

        res = []
        for candidate in (candidate1, candidate2):
            if candidate is not None and nums.count(candidate) > (len(nums) // 3):
                res.append(candidate)

        return res

def solve():
    #nums = list(map(int, sys.stdin.read().strip().split()))
    nums = [1, 2, 3, 1, 2, 1, 1]
    solution = Solution()
    print(solution.majorityElement(nums))

if __name__ == "__main__":
    solve()

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = -1

        total_sum = sum(nums)
        left = 0

        for i in range(len(nums)):
            if left == (total_sum - left - nums[i]):
                return i
            left += nums[i]
        return -1
solution = Solution()
print(solution.pivotIndex([1,7,3,6,5,6]))
print(solution.pivotIndex([1,2,3]))
print(solution.pivotIndex([2, 1, -1]))
